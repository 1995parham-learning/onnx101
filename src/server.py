import onnxruntime as ort

# Load the model and create InferenceSession
model_path = "./model.onnx"
session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])

outputs = session.run(output_names={}, input_feed={})
print(outputs)
