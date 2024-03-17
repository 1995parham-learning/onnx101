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

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/1995parham-learning/onnx101" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

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
