# -*- coding: utf-8 -*-
"""
SI Pool
========
Modified: 2021-11

This module stores and performs operations on a set of neuron objects to extract correlational data.

Dependancies
------------
>>> import logging.config
>>> from threading import Thread
>>> from ecp.memory.matrix_memory import MatrixMap
>>> from ecp.network.neuron import Neuron

Copyright © 2021 LEAP Systems. All Rights Reserved.
"""
import os
import logging.config

from threading import Thread
from sia.neuron import Neuron
from sia.network import Network

class Pool:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("%s Instantiation successful", self)

    def populate(self, input_set):
        self.log.debug("Input set: %s", input_set)
        # drop each neuron sequentially into the pool 
        # set.pop randomly pops an element from the set
        for _ in range(len(input_set)):
            neuron = Neuron(input_set.pop())
            Network.neurons.append(neuron)
        self.log.debug("Pool populated with %s neurons", len(Network.neurons))
    
    def synapse(self, neurons:set, func, *argv, **kwargs):
        """
        """
        synapses = list()
        for neuron in neurons:
            synapses.append(Thread(name=neuron, target=func(neuron), args=(*argv, *kwargs), daemon=True))
            synapses[-1].start()
            self.log.debug("Started %s activation function for: %s", func(neuron).__name__, neuron)
        # wait for all active threads to converge 
        for worker in synapses:
            worker.join(timeout=1.0)
            self.log.debug("Thread %s joined", worker)