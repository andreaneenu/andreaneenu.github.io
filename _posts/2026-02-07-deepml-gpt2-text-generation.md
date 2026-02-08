---
layout: post
title: "Deep-ML: GPT-2 Text Generation"
date: 2026-02-07 12:44:21
description: Building GPT-2 text generation from scratch - understanding transformers, embeddings, and layer normalization
tags: deep-ml machine-learning gpt2 transformers nlp deep-learning text-generation language-models
categories: deep-ml-journey
giscus_comments: true
related_posts: true
---

## Introduction

I recently tackled the **GPT-2 Text Generation** problem on [deep-ml.ai](https://www.deep-ml.com/problems/88?from=Deep%20Learning), a hard-level challenge focusing on implementing the core components of transformer-based language models. This problem required building text generation from scratch, giving me deep insights into how GPT-2 actually works under the hood.

## The Problem

**Difficulty**: Hard  
**Link**: [https://www.deep-ml.com/problems/88](https://www.deep-ml.com/problems/88?from=Deep%20Learning)

The challenge was to implement GPT-2's text generation mechanism, including:
- Token and positional embeddings
- Layer normalization
- Autoregressive text generation
- Logit calculation and token selection

This problem strips away the high-level abstractions and forces you to understand the fundamental operations that make GPT-2 work.

## My Approach

My implementation focused on building the core pipeline step by step:

### 1. **Embedding Layer**
I combined word token embeddings (`wte`) with positional encodings (`wpe`) to give each token both semantic meaning and positional context:

```python
x = params["wte"][tokens] + params["wpe"][:seq_len]
```

This is crucial because transformers don't inherently understand token order - positional encodings provide that information.

### 2. **Layer Normalization**
One of the trickiest parts was implementing layer normalization correctly. The key insight is that normalization must be applied **per token** (per row), not across the entire matrix:

```python
def layernorm(x, g, b, epsilon=1e-5):
    return g*((x-np.mean(x))/np.sqrt(np.var(x)+epsilon))+b
```

Applying it incorrectly would mix statistics across different tokens, breaking the model's behavior.

### 3. **Autoregressive Generation**
The generation loop iteratively produces one token at a time, using all previous tokens as context:

```python
for i in range(n_tokens_to_generate):
    seq_len = len(tokens)
    x = params["wte"][tokens] + params["wpe"][:seq_len]
    for i in range(len(x)):
        x[i] = layernorm(x[i], params["ln_f"]["g"], params["ln_f"]["b"])
    logits = x @ params["wte"].T
    next_token = int(np.argmax(logits[-1]))
    tokens.append(next_token)
```

### 4. **Greedy Decoding**
I used greedy decoding (selecting the highest probability token) for simplicity and determinism:

```python
next_token = int(np.argmax(logits[-1]))
```

## What I Learned

This problem taught me several fundamental concepts:

- **Embeddings are additive**: Token and positional embeddings are simply added together, which works because the model learns to use different dimensions for different purposes
- **Layer normalization mechanics**: Understanding the exact mathematical operations and why they're applied per token
- **Autoregressive generation**: How language models generate text one token at a time, with each prediction depending on all previous tokens
- **The simplicity of the core loop**: Despite GPT-2's complexity, the basic generation loop is surprisingly straightforward

## Cool Aspects 

What I found most fascinating:

1. **Layer normalization's importance**: Such a simple operation (normalize, scale, shift) has such a profound impact on training stability and model performance

2. **Greedy vs. sampling trade-offs**: While I used greedy decoding, understanding that temperature sampling and top-k/top-p sampling can dramatically change output quality and diversity

3. **Building intuition**: Implementing from scratch gave me a much deeper understanding than just using `transformers.pipeline()`

## Challenges & Solutions

**Challenge**: Layer normalization axis confusion  
**Solution**: Carefully reviewed the mathematical definition and ensured normalization was applied per row (per token). Testing with known inputs helped verify correctness.

**Challenge**: Managing token indices correctly  
**Solution**: Tracked the initial prompt length separately to ensure only generated tokens were returned, not the entire sequence including the prompt.

**Challenge**: Understanding the flow of data  
**Solution**: Watched [Andrej Karpathy's excellent GPT video](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1193s) which provided invaluable intuition about how transformers process information.

## Key Takeaways

1. **Implementation builds intuition**: Writing GPT-2 from scratch gave me insights no amount of reading could provide

2. **Details matter**: Small mistakes like normalizing across the wrong axis can completely break the model

3. **Simplicity at the core**: Despite the hype around transformers, the fundamental operations are matrix multiplications, additions, and normalizations

4. **Testing is crucial**: Setting random seeds and testing with known inputs is essential for debugging generative models

## Related Resources

- [Problem on deep-ml.ai](https://www.deep-ml.com/problems/88?from=Deep%20Learning)
- [My solution on GitHub](https://github.com/andreaneenu/deep-ml_work)
- [Andrej Karpathy's GPT Video](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1193s) - Highly recommended!
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original Transformer paper
- [GPT-2 Paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

---

**Tags**: deep-ml machine-learning gpt2 transformers nlp deep-learning text-generation language-models

