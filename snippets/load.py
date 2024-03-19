import pickle

import onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

if __name__ == "__main__":
    MODEL = None
    with open("model.pkl", "rb") as f:
        MODEL = pickle.load(f)
    assert MODEL is not None

    INITIAL_TYPE = [("float_input", FloatTensorType([None, 7]))]
    ONX = convert_sklearn(MODEL, initial_types=INITIAL_TYPE)
    onnx.save_model(
        ONX,
        "model.onnx",
        save_as_external_data=True,
        all_tensors_to_one_file=True,
        location="filename",
        size_threshold=1024,
        convert_attribute=False,
    )
