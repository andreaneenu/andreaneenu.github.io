---
description: Automate deep-ml work documentation and blog generation
---

# Deep-ML Work Documentation Agent

This workflow automates the process of documenting your learning from deep-ml.ai challenges by:
1. Creating/updating code in a dedicated GitHub repository (`deep-ml_work`)
2. Generating blog posts for your personal website based on your learnings
3. Ensuring proper review before pushing changes

## Prerequisites

Before running this workflow, ensure you have:
- [ ] Created the `deep-ml_work` repository on GitHub
- [ ] Cloned the repository locally (recommended location: `c:\Users\andre\deep-ml_work`)
- [ ] Git configured with your credentials
- [ ] Your personal website repository accessible at `c:\Users\andre\andreaneenu.github.io`

## Workflow Steps

### Step 1: Gather Information

The agent will ask you for the following information:
- **Problem Title**: The name/title of the deep-ml problem you solved
- **Problem URL**: Link to the problem on deep-ml.ai
- **Difficulty Level**: Easy/Medium/Hard
- **Topics/Tags**: Relevant topics (e.g., machine-learning, neural-networks, optimization, numpy, linear-algebra)
- **Your Code**: The solution code you wrote
- **Programming Language**: Language used (e.g., Python, JavaScript)
- **Key Learnings**: What you learned from this problem
- **Cool Aspects**: What you found interesting or cool about the problem
- **Takeaways**: Main takeaways and insights
- **Challenges Faced**: Any difficulties you encountered and how you overcame them

### Step 2: Organize Code in deep-ml_work Repository

The agent will:
1. Navigate to your `deep-ml_work` repository
2. Create a structured directory based on the problem topic (e.g., `neural-networks/`, `optimization/`)
3. Create a solution file with proper naming: `{problem-slug}.{ext}` (e.g., `matrix-multiplication.py`)
4. Add a README.md in the problem directory with:
   - Problem description and link
   - Approach explanation
   - Key insights
5. Update the main repository README.md with a link to the new solution
6. Stage the changes for review

**Directory Structure Example:**
```
deep-ml_work/
├── README.md (index of all solutions)
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

### Step 3: Generate Blog Post

The agent will create a blog post in your personal website repository with:

**File Location**: `_posts/YYYY-MM-DD-deepml-{problem-slug}.md`

**Front Matter**:
```yaml
---
layout: post
title: "Deep-ML: {Problem Title}"
date: YYYY-MM-DD HH:MM:SS
description: {Brief description of what you learned}
tags: deep-ml machine-learning {additional-tags}
categories: deep-ml-journey
giscus_comments: true
related_posts: true
---
```

**Blog Content Structure**:
1. **Introduction**: Brief overview of the problem
2. **The Problem**: Description and link to deep-ml.ai
3. **My Approach**: How you solved it
4. **Code Solution**: Embedded code with syntax highlighting
5. **What I Learned**: Key learnings and insights
6. **Cool Aspects**: Interesting things you discovered
7. **Challenges & Solutions**: Difficulties faced and how you overcame them
8. **Key Takeaways**: Main lessons learned
9. **Related Resources**: Links to documentation, papers, or related problems

### Step 4: Review Changes

The agent will:
1. Show you a summary of all changes:
   - New files created in `deep-ml_work`
   - Blog post content
   - Updated README files
2. Ask for your approval before proceeding
3. Allow you to request modifications if needed

### Step 5: Commit and Push

After your approval, the agent will:

**For deep-ml_work repository:**
```bash
cd c:\Users\andre\deep-ml_work
git add .
git commit -m "Add solution: {Problem Title} - {Topics}"
git push origin main
```

**For personal website:**
```bash
cd c:\Users\andre\andreaneenu.github.io
git add _posts/YYYY-MM-DD-deepml-{problem-slug}.md
git commit -m "Add blog post: Deep-ML {Problem Title}"
git push origin main
```

### Step 6: Confirmation

The agent will:
1. Confirm successful pushes to both repositories
2. Provide links to:
   - The new solution in your deep-ml_work repo
   - The blog post (once your website rebuilds)
3. Suggest next steps (e.g., share on social media, update portfolio)

## Usage Example

To use this workflow, simply say:
```
/deepml
```

Or provide details directly:
```
I just solved the "Implement Backpropagation" problem on deep-ml. 
Can you help me document it using the /deepml workflow?
```

## Customization Options

You can customize the workflow by:
- **Changing repository locations**: Update paths in the workflow
- **Modifying blog template**: Adjust the blog post structure
- **Adding more metadata**: Include additional fields like related papers, datasets used, etc.
- **Custom tags**: Define your own tagging system
- **Code formatting**: Specify preferred code style or linting rules

## Additional Features

### Auto-Generate Problem Categories

The agent can automatically suggest categories based on:
- Problem difficulty
- Topics covered
- Algorithms used
- Data structures involved

### Link Related Problems

The agent can:
- Find related problems you've solved previously
- Add links to related blog posts
- Suggest next problems to try

### Generate Social Media Snippets

The agent can create ready-to-share snippets for:
- Twitter/X
- LinkedIn
- Dev.to
- Medium

### Track Progress

The agent maintains a progress tracker in your deep-ml_work README:
- Total problems solved
- Breakdown by difficulty
- Topics covered
- Streak information

## Tips for Best Results

1. **Be Specific**: Provide detailed information about your learnings
2. **Include Context**: Explain why the problem was interesting
3. **Show Your Process**: Don't just show the final solution, explain your journey
4. **Add Visuals**: Consider adding diagrams or visualizations to your blog posts
5. **Cross-Reference**: Link to related problems and concepts
6. **Keep It Updated**: Regularly update your progress tracker

## Troubleshooting

### Repository Not Found
If the deep-ml_work repository doesn't exist:
```bash
cd c:\Users\andre
git clone https://github.com/YOUR_USERNAME/deep-ml_work.git
```

### Merge Conflicts
If you encounter merge conflicts:
1. The agent will notify you
2. You'll need to resolve conflicts manually
3. Re-run the workflow after resolution

### Blog Not Showing
If your blog post doesn't appear:
- Check that `published: true` (or the field is omitted)
- Verify the date is not in the future
- Ensure the filename follows the correct format
- Check for YAML syntax errors in front matter

## Future Enhancements

Potential additions to this workflow:
- [ ] Automatic screenshot capture from deep-ml.ai
- [ ] Integration with LeetCode/HackerRank for cross-platform documentation
- [ ] Generate comparison with other solutions
- [ ] Create visualization of algorithm complexity
- [ ] Auto-generate test cases
- [ ] Integration with Notion or other note-taking apps
- [ ] Weekly/monthly summary blog posts
- [ ] Performance benchmarking across solutions