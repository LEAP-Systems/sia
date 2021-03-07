# -*- coding: utf-8 -*-
"""
SI Neuron
=========
Modified: 202-11

This module defines the fundamental unit of SIA based operations. Each neuron is encoded with a set of
unique activation functions which allow them to combine and form networks for analysis.

Dependancies
------------
>>> import logging.config
>>> import numpy as np

Copyright © 202 LEAP Systems. All Rights Reserved.
"""

import logging.config

from sia.network import Network

class Neuron:
    def __init__(self, value:int):
        self.log = logging.getLogger(__name__)
        self.value = value
        self.upper = None
        self.lower = None
        self.stable = False
        self.log.debug("%s instantiation successful", self)

    def activation(self):
        # iterate over neurons in pool
        for neuron in Network.neurons:
            # in search of smallest number which satisfies bound
            if neuron.value > self.value:
                if self.upper is None or self.upper.value > neuron.value:
                    self.upper = neuron
                    self.log.debug("Assigned upper connection to %s with a value %s > %s", self.upper, self.upper.value, self.value)
            # in search of largest number which satisfies bound
            elif neuron.value < self.value:
                if self.lower is None or self.lower.value < neuron.value:
                    self.lower = neuron
                    self.log.debug("Assigned lower connection to %s with a value %s < %s", self.lower, self.lower.value, self.value)
        self.stable = True
        self.log.debug("%s activation complete", self)

    def __repr__(self) -> str:
        if self.upper is None:
            upper = None
        else:
            upper = self.upper.value
        
        if self.lower is None:
            lower = None
        else:
            lower = self.lower.value

        return "Neuron({} > {} > {})".format(lower, self.value, upper)
