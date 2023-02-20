#!/bin/bash
IN_DATA=$1
KMER=$2
START_TIME=$(uptime | awk '{print($1)}')
START=$SECONDS

if [ $1 = "-h" ]
then
	echo "Usage:"
	echo "./fake_assembly.sh <sequencing_reads>.fastq <kmer size>"
	echo
	echo "Where you need to replace <sequencing_reads> with your actual sequencing reads file and replace <kmer size> with the kmer size you want to use to run the assembly (either 31 or 51)"
	exit 
fi


echo "Starting the assembly of your genome at ${START_TIME}"
sleep 3
echo "Sequencing data will be retrieved from ${IN_DATA} file..."
sleep 5


case ${KMER} in
	31 ) 
		echo "Assembling with kmer=31"
		sleep 120 
		echo "Assembly produced 1300 contigs"
		;;
	51 )
		echo "Assembling with kmer=51"
		sleep 90
		echo "Assembly produced 2000 contigs"
		;;
	* ) 
		echo "kmer size unknown"
		;;
esac

DURATION=$(expr $SECONDS - ${START})
echo "Run time was ${DURATION} seconds"
