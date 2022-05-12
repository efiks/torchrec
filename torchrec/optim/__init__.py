#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Torchrec Optimizers

Torchrec contains a special optimizer called KeyedOptimizer. KeyedOptimizer exposes the state_dict with meaningful keys- it enables  loading both
torch.tensor and `ShardedTensor <https://github.com/pytorch/pytorch/issues/55207>`_ in place, and it prohibits loading an empty state into already initialized KeyedOptimizer and vise versa.

It also contains several modules wrapping KeyedOptimizer, called CombinedOptimizer and OptimizerWrapper
"""

from torchrec.optim.clipping import GradientClipping, GradientClippingOptimizer  # noqa
from torchrec.optim.fused import FusedOptimizer, FusedOptimizerModule  # noqa
from torchrec.optim.keyed import (  # noqa
    CombinedOptimizer,
    KeyedOptimizer,
    KeyedOptimizerWrapper,
    OptimizerWrapper,
)
from torchrec.optim.warmup import WarmupOptimizer, WarmupPolicy, WarmupStage  # noqa

from . import clipping, fused, keyed, warmup  # noqa  # noqa  # noqa  # noqa