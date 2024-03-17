---
theme: seriph
title: ONNX 101
info: |
  ONNX Crash Course
  By Elahe Dastan
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# ONNX Crash Course

By Elahe Dastan

---

# What is ONNX?

ONNX can be compared to a **programming language** specialized in mathematical functions.
It defines all the necessary operations a machine learning model needs to implement
its inference function with this language.

```python
def onnx_linear_regressor(X):
    "ONNX code for a linear regression"
    return onnx.Add(onnx.MatMul(X, coefficients), bias)
```
