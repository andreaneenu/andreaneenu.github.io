#!/usr/bin/env python3
"""
Deep-ML Documentation Helper Script
Utility functions for automating deep-ml work documentation
"""

import os
import re
from datetime import datetime
from pathlib import Path


def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def get_file_extension(language):
    """Get file extension based on programming language"""
    extensions = {
        'python': 'py',
        'javascript': 'js',
        'java': 'java',
        'cpp': 'cpp',
        'c++': 'cpp',
        'c': 'c',
        'go': 'go',
        'rust': 'rs',
        'typescript': 'ts',
        'ruby': 'rb',
        'r': 'r',
        'julia': 'jl',
    }
    return extensions.get(language.lower(), 'txt')


def create_solution_readme(problem_info):
    """Generate README content for solution directory"""
    readme = f"""# {problem_info['title']}

**Difficulty**: {problem_info['difficulty']}  
**Topics**: {', '.join(problem_info['tags'])}  
**Problem Link**: [{problem_info['url']}]({problem_info['url']})

## Problem Description

{problem_info.get('description', 'See problem link for full description.')}

## My Approach

{problem_info['approach']}

## Complexity Analysis

- **Time Complexity**: {problem_info.get('time_complexity', 'O(?)')}
- **Space Complexity**: {problem_info.get('space_complexity', 'O(?)')}

## Key Insights

{problem_info['key_learnings']}

## Challenges Faced

{problem_info.get('challenges', 'No major challenges encountered.')}

## Solution

See `solution.{get_file_extension(problem_info['language'])}` for the complete implementation.

---

*Solved on {datetime.now().strftime('%B %d, %Y')}*
"""
    return readme


def create_blog_post(problem_info):
    """Generate blog post content"""
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    slug = slugify(problem_info['title'])
    
    # Prepare tags
    tags = ['deep-ml', 'machine-learning'] + problem_info['tags']
    tags_str = ' '.join(tags)
    
    blog_content = f"""---
layout: post
title: "Deep-ML: {problem_info['title']}"
date: {date_str}
description: {problem_info.get('description', f"My solution and learnings from the {problem_info['title']} problem on deep-ml.ai")}
tags: {tags_str}
categories: deep-ml-journey
giscus_comments: true
related_posts: true
---

## Introduction

I recently tackled the **{problem_info['title']}** problem on [deep-ml.ai]({problem_info['url']}), a {problem_info['difficulty'].lower()}-level challenge focusing on {', '.join(problem_info['tags'][:3])}. This post documents my approach, learnings, and key takeaways.

## The Problem

**Difficulty**: {problem_info['difficulty']}  
**Link**: [{problem_info['url']}]({problem_info['url']})

{problem_info.get('problem_description', 'The problem requires implementing a solution that demonstrates understanding of core machine learning concepts.')}

## My Approach

{problem_info['approach']}

## Code Solution

Here's my implementation in {problem_info['language']}:

```{problem_info['language'].lower()}
{problem_info['code']}
```

## What I Learned

{problem_info['key_learnings']}

## Cool Aspects 🎯

{problem_info['cool_aspects']}

## Challenges & Solutions

{problem_info.get('challenges', 'The implementation was straightforward once I understood the core concepts.')}

## Complexity Analysis

- **Time Complexity**: `{problem_info.get('time_complexity', 'O(?)')}`
- **Space Complexity**: `{problem_info.get('space_complexity', 'O(?)')}`

{problem_info.get('complexity_explanation', '')}

## Key Takeaways

{problem_info['takeaways']}

## Related Resources

- [Problem on deep-ml.ai]({problem_info['url']})
- [My solution on GitHub](https://github.com/andreaneenu/deep-ml_work)

---

**Tags**: {tags_str}

*What deep-ml problems have you solved recently? Share your experiences in the comments below!*
"""
    return blog_content, slug


def update_main_readme(repo_path, problem_info):
    """Update the main README.md with new solution entry"""
    readme_path = Path(repo_path) / 'README.md'
    
    # Create README if it doesn't exist
    if not readme_path.exists():
        initial_content = """# Deep-ML Solutions

This repository contains my solutions to problems from [deep-ml.ai](https://deep-ml.ai), documenting my journey in learning machine learning fundamentals.

## 📊 Progress Tracker

- **Total Problems Solved**: 0
- **Easy**: 0
- **Medium**: 0
- **Hard**: 0

## 🗂️ Solutions by Topic

### Neural Networks
*No solutions yet*

### Optimization
*No solutions yet*

### Linear Algebra
*No solutions yet*

### Statistics & Probability
*No solutions yet*

## 📝 All Solutions

| # | Problem | Difficulty | Topics | Solution |
|---|---------|------------|--------|----------|

---

*Last updated: {datetime.now().strftime('%B %d, %Y')}*
"""
        readme_path.write_text(initial_content)
    
    # Read current content
    content = readme_path.read_text()
    
    # Update progress tracker
    # This is a simplified version - you'd want more robust parsing
    
    # Add new solution to table
    slug = slugify(problem_info['title'])
    category = problem_info['tags'][0] if problem_info['tags'] else 'general'
    solution_link = f"[Solution](./{category}/{slug}/)"
    
    new_row = f"| - | {problem_info['title']} | {problem_info['difficulty']} | {', '.join(problem_info['tags'][:3])} | {solution_link} |\n"
    
    # Insert before the "Last updated" line
    content = content.replace(
        f"---\n\n*Last updated:",
        f"{new_row}\n---\n\n*Last updated:"
    )
    
    # Update timestamp
    old_timestamp = re.search(r'\*Last updated: .*\*', content)
    if old_timestamp:
        content = content.replace(
            old_timestamp.group(0),
            f"*Last updated: {datetime.now().strftime('%B %d, %Y')}*"
        )
    
    readme_path.write_text(content)
    return True


def create_directory_structure(repo_path, problem_info):
    """Create the directory structure for the solution"""
    category = slugify(problem_info['tags'][0]) if problem_info['tags'] else 'general'
    problem_slug = slugify(problem_info['title'])
    
    solution_dir = Path(repo_path) / category / problem_slug
    solution_dir.mkdir(parents=True, exist_ok=True)
    
    return solution_dir


def save_solution_files(solution_dir, problem_info):
    """Save solution code and README to the directory"""
    # Save code file
    ext = get_file_extension(problem_info['language'])
    code_file = solution_dir / f"solution.{ext}"
    code_file.write_text(problem_info['code'])
    
    # Save README
    readme_file = solution_dir / "README.md"
    readme_content = create_solution_readme(problem_info)
    readme_file.write_text(readme_content)
    
    return code_file, readme_file


def get_blog_filename(problem_info):
    """Generate blog post filename"""
    date_str = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(problem_info['title'])
    return f"{date_str}-deepml-{slug}.md"


if __name__ == "__main__":
    print("Deep-ML Documentation Helper Script")
    print("This script provides utility functions for the deep-ml workflow.")
    print("Import these functions in your automation scripts.")
