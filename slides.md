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
favicon: "https://github.com/1995parham-me.png"
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

## What is ONNX?

ONNX can be compared to a **programming language** specialized in mathematical functions.
It defines all the necessary operations a machine learning model needs to implement
its _inference function_ with this language.

```python
def onnx_linear_regressor(X):
    "ONNX code for a linear regression"
    return onnx.Add(onnx.MatMul(X, coefficients), bias)
```

---

## ONNX Runtime

ONNX Runtime provides an easy way to run machine _learned models_ with high performance on **CPU** or **GPU**
without dependencies on the training framework.

Machine learning frameworks are usually optimized for _batch training rather than for prediction_,
which is a more common scenario in applications, sites, and services. At a high level, you can:

<v-clicks>

- Train a model using your _favorite framework_. <twemoji-teacher />
- Convert or export the model into _ONNX format_. <twemoji-package />
- Load and run the model using _ONNX Runtime_. <twemoji-rocket />

</v-clicks>
