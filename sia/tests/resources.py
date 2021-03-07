# -*- coding: utf-8 -*-
"""
Test Data Generation
====================

Copyright © 2021 LEAP Systems. All Rights Reserved.
"""

import random


class Resources:

    def generate(sample:int, rng:int) -> list:
        return [ int(random.uniform(0, 1)*rng) for _ in range(0,sample) ]

    sortint128 = generate(128,1000)