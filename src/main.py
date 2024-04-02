"""
To reduce the time, we create and load onnx model
in the same script. The example is written based on:

https://onnx.ai/sklearn-onnx/auto_tutorial/plot_abegin_convert_pipeline.html
"""

import pickle

import numpy
import onnxruntime as ort
from skl2onnx import to_onnx

import onnx.reference

if __name__ == "__main__":
    # load trained model from a pickle file.
    MODEL = None
    with open("model.pkl", "rb") as f:
        MODEL = pickle.load(f)

    assert MODEL is not None

    # create a sample train data.
    x_sample = numpy.array([[12.3, 24.4, 45.3, 65.7, 567, 4.5, 1]])

    # calls convert_sklearn() with simplified parameters.
    onx = to_onnx(MODEL, x_sample[:1].astype(numpy.float64))

    session_options = ort.SessionOptions()
    session_options.graph_optimization_level = (
        ort.GraphOptimizationLevel.ORT_DISABLE_ALL
    )

    oinf = onnx.reference.ReferenceEvaluator(onx)
    print(oinf)
