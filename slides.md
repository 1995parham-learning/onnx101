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
layout: cover
hideInToc: true
---

# ONNX Crash Course

By Elahe Dastan

<div class="abs-br m-6 flex">
  <a href="https://github.com/1995parham-learning/onnx101" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---

<Toc mode="" />

---
layout: center
---

# ONNX <twemoji-thinking-face />

Why you may use something else instead of serving your model by yourself?

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

<img alt="linreg" src="/linreg1.png" class="rounded mx-auto d-block shadow h-60" />

---

## Serialization with `protobuf`

The deployment of a machine-learned model into production usually requires **replicating** the entire ecosystem
used to train the model, most of the time with a _docker_.

```toml
[packages]
numpy = "*"
scikit-learn = "1.3.2"
uvicorn = { extras = ["standard"], version = "*" }
cloudpickle = "*"
flask = "*"
sqlalchemy = { extras = ["mypy"], version = "*" }
psycopg2-binary = "*"
prometheus-client = "*"
fastapi = "*"
pandas = "*"
matplotlib = "*"
jupyter = "*"
keras = "*"
prometheus-fastapi-instrumentator = "*"
```

---
hideInToc: true
---

## Serialization with `protobuf` (Cont'd)

Once a model is converted into ONNX, the production environment only needs a **runtime** to execute the graph
defined with ONNX operators.

This runtime can be developed in any language suitable for the production application,
C, java, python, JavaScript, C#, Web Assembly, ARM, etc.

::Note
But to make that happen, the ONNX graph needs to be saved.
ONNX uses `protobuf` to serialize the graph into one single block.
It aims at optimizing the model size as much as possible.
::

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
