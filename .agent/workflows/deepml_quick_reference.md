# Deep-ML Workflow Quick Reference

## Quick Start

To use the deep-ml documentation workflow:

```
/deepml
```

Then provide the information when prompted, or provide it all at once.

## Information Checklist

When documenting a deep-ml problem, have ready:

- [ ] Problem title
- [ ] Problem URL from deep-ml.ai
- [ ] Difficulty level (Easy/Medium/Hard)
- [ ] Your solution code
- [ ] Programming language used
- [ ] Topics/tags (e.g., neural-networks, optimization, linear-algebra)
- [ ] Your approach/methodology
- [ ] Key learnings
- [ ] Cool/interesting aspects
- [ ] Main takeaways
- [ ] Challenges faced (optional)
- [ ] Time complexity (optional)
- [ ] Space complexity (optional)

## Common Tags

Use these tags for consistency:

### Topics
- `neural-networks`
- `deep-learning`
- `optimization`
- `gradient-descent`
- `backpropagation`
- `linear-algebra`
- `matrix-operations`
- `statistics`
- `probability`
- `calculus`
- `numpy`
- `data-preprocessing`
- `feature-engineering`
- `model-evaluation`
- `loss-functions`
- `activation-functions`
- `regularization`
- `dimensionality-reduction`

### Difficulty
- `easy`
- `medium`
- `hard`

### Special Tags
- `mathematics`
- `implementation`
- `algorithm`
- `performance`
- `numerical-methods`

## File Naming Conventions

### Blog Posts
Format: `YYYY-MM-DD-deepml-{problem-slug}.md`

Example: `2026-02-07-deepml-matrix-multiplication.md`

### Solution Files
Format: `solution.{ext}`

Examples:
- `solution.py` (Python)
- `solution.js` (JavaScript)
- `solution.cpp` (C++)

### Directories
Format: `{topic}/{problem-slug}/`

Example: `linear-algebra/matrix-multiplication/`

## Git Commit Messages

### For Solutions
```
Add solution: {Problem Title} - {Topics}
```

Example:
```
Add solution: Matrix Multiplication - Linear Algebra, NumPy
```

### For Blog Posts
```
Add blog post: Deep-ML {Problem Title}
```

Example:
```
Add blog post: Deep-ML Matrix Multiplication
```

## Repository Structure

```
deep-ml_work/
├── README.md                          # Main index
├── neural-networks/
│   ├── backpropagation/
│   │   ├── solution.py
│   │   └── README.md
│   └── activation-functions/
│       ├── solution.py
│       └── README.md
├── optimization/
│   └── gradient-descent/
│       ├── solution.py
│       └── README.md
└── linear-algebra/
    └── matrix-operations/
        ├── solution.py
        └── README.md
```

## Blog Post Front Matter Template

```yaml
---
layout: post
title: "Deep-ML: {Problem Title}"
date: YYYY-MM-DD HH:MM:SS
description: {Brief description}
tags: deep-ml machine-learning {additional-tags}
categories: deep-ml-journey
giscus_comments: true
related_posts: true
---
```

## Workflow Steps Summary

1. **Gather Info** - Collect all problem details
2. **Create Solution** - Add code to deep-ml_work repo
3. **Generate Blog** - Create blog post in website repo
4. **Review** - Check all changes
5. **Commit & Push** - Push to both repositories
6. **Confirm** - Verify successful deployment

## Useful Commands

### Check Repository Status
```bash
cd c:\Users\andre\deep-ml_work
git status
```

### View Recent Commits
```bash
git log --oneline -5
```

### Preview Blog Locally
```bash
cd c:\Users\andre\andreaneenu.github.io
bundle exec jekyll serve
```

Then visit: http://localhost:4000

## Tips

1. **Be Detailed**: More context = better blog posts
2. **Use Code Blocks**: Always use proper syntax highlighting
3. **Add Visuals**: Consider adding diagrams for complex concepts
4. **Link Resources**: Reference documentation and papers
5. **Cross-Reference**: Link to related problems you've solved
6. **Update Tags**: Keep your tag list in `_config.yml` updated
7. **Test Locally**: Preview blog posts before pushing
8. **Consistent Naming**: Use kebab-case for slugs

## Troubleshooting

### Blog Not Showing Up
- Check `published: true` or omit the field
- Verify date is not in the future
- Check filename format: `YYYY-MM-DD-title.md`
- Look for YAML syntax errors

### Repository Not Found
```bash
# Clone the repository
cd c:\Users\andre
git clone https://github.com/andreaneenu/deep-ml_work.git
```

### Merge Conflicts
```bash
# Pull latest changes first
git pull origin main

# Resolve conflicts manually
# Then commit and push
git add .
git commit -m "Resolve merge conflicts"
git push origin main
```

## Contact & Support

For issues with the workflow, check:
1. Workflow documentation: `.agent/workflows/deepml.md`
2. Helper script: `.agent/workflows/deepml_helper.py`
3. Templates: `.agent/workflows/deepml_*.md`

---

*Happy Learning! 🚀*
