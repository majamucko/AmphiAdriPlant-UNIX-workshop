import os
import sys
import matplotlib.pyplot as plt
from Bio import SeqIO
from merge_images import merge_images

def draw_rectangles(genes_list, out_file="out.png"):
    
    # define genes colors
    COLORS = {"CYTB": "red", "ND4L": "blue", "COX2": "green"} 
    
    # create fig and axes and set layout as constrained (to keep neighbors
    # genes from overlapping)
    fig, axs = plt.subplots(1, len(genes_list), constrained_layout=True)
    
    # draw genes (each ax is a gene) 
    curr_x = 0
    c = 0 # keeps track of gene position in genes_list
    for ax in axs.flat:
        gene = genes_list[c]
        
        # set gene color
        if gene not in COLORS:
            color = "grey"
        else:
            color = COLORS[gene]
        
        props = dict(facecolor=color, alpha=0.7, pad=1.5) # set text properties
        text = ax.text(0.5, 0.5, gene, ha="center", bbox=props) # draw text
        ax.set_axis_off() # remove x/y axis 
        c += 1 # update c value to go to next gene
    
    # plot figure title (will be centered)
    fig.suptitle(out_file, x=0.5, y=0.85, ha='left', va='center') 
    # set figure height to keep big vertical whitespace from being drawn
    fig.set_figheight(1)
    # save figure
    plt.savefig(out_file)

def get_gene_list(genbank_file):
    
    genes_list = []
    for _, record in enumerate(SeqIO.parse(genbank_file, "genbank")):
        for feature in record.features:
            if feature.type == 'CDS':
                gene_name = feature.qualifiers["gene"][0]
                gene_start = int(feature.location.start)
                genes_list.append([gene_name, gene_start])
    
    # sort genes to get a list in ascending order of start position 
    # of the features (prevents a gene in the end position of the sequence
    # but wrongly placed at the begginning of the genbank file to be shown first
    genes_list.sort(key = lambda x: x[1])
    
    final_list = [gene[0] for gene in genes_list]    
    
    return final_list


def parse_genbank_files(genbank_list):
    
    individual_plot_files = []   
    with open(genbank_list, "r") as f:
        for line in f:
            genbank_file = line.strip()
            genes_list = get_gene_list(genbank_file)
            out_plot_filename = f"{genbank_file}.genes.png"
            draw_rectangles(genes_list, out_plot_filename)
            individual_plot_files.append(out_plot_filename)
    
    merge_images(individual_plot_files, "all_seqs.png")    

if __name__ == "__main__":
    
    
    in_genbank = sys.argv[1]
    parse_genbank_files(in_genbank)
