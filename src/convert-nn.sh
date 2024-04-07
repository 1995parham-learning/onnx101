#!/usr/bin/env bash

python -m tf2onnx.convert --saved-model nn-model --output model.onnx
