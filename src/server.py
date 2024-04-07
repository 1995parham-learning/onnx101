"""
Load the model using ONNX runtime.
"""

import onnxruntime as ort

if __name__ == "__main__":
    # Load the model and create InferenceSession
    MODEL_PATH = "./model.onnx"
    session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])

    # Call Nostradamus model
    outputs = session.run(
        output_names={},
        input_feed={
            "haversine_distance_layer_input": [
                [
                    32.058145,
                    44.326834,
                    32.028416,
                    44.333983,
                    10.500000,
                    3.373689638972256,
                    1,
                ]
            ]
        },
    )
    print(outputs)
