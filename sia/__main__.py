# -*- coding: utf-8 -*-
"""
Swarm of Intelligent Agents 
===========================
Modified: 2021-03

Copyright © 2021 LEAP Systems. All Rights Reserved.
"""
import sys
import time
import logging.config

from sia.pool import Pool
from sia.tests.resources import Resources
from sia.tests.merge_sort import mergeSort
from sia.network import Network

log = logging.getLogger(__name__)

try:
    sample = int(sys.argv[1])
    rng = int(sys.argv[2])
except IndexError:
    # set default when running with no args
    input_set = Resources.sortint128
    log.info("Executing defaults with 128 agents with integers in range [ 0,1000 ]")
else:
    input_set = Resources.generate(sample, rng)
    log.info("Executing with %s agents with integers in range [ 0,%s ]", sample, rng)

pool = Pool()
pool.populate(input_set)

start = time.time()
pool.synapse(Network.neurons, lambda neuron : neuron.activation)
end = time.time()
log.info("SIA elapsed execution time: %s ms", round((end-start)*1000,4))

start = time.time()
mergeSort(input_set)
end = time.time()
log.info("Merge sort elapsed execution time: %s ms", round((end-start)*1000,4))