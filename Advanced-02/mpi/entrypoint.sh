#!/bin/sh

# Making sure that all the pods have been spawned before starting
sleep 5

mpirun --allow-run-as-root -n 2 osu-7.3/c/mpi/pt2pt/standard/osu_latency -i 100 -x 500

mpirun --allow-run-as-root -n 2 osu-7.3/c/mpi/collective/blocking/osu_scatter -i 100 -x 500

