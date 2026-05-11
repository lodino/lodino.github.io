# Personal Website Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the approved compact, photo-first two-column researcher homepage for `lodino.github.io`.

**Architecture:** Add a dedicated Jekyll homepage layout and a focused Sass partial. Reuse existing `_publications` collection content for selected publications and leave the rest of the Academic Pages theme intact.

**Tech Stack:** Jekyll, Liquid, Sass, existing Minimal Mistakes / Academic Pages theme.

---

### Task 1: Homepage Layout Contract

**Files:**
- Create: `tests/test_homepage_design.py`
- Create: `_layouts/research_home.html`
- Modify: `_pages/about.md`
- Create: `_sass/_research-home.scss`
- Modify: `assets/css/main.scss`

- [ ] **Step 1: Write the failing test**

Create `tests/test_homepage_design.py` with checks that the homepage uses the new layout, imports the homepage styles, and exposes the required semantic sections.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 tests/test_homepage_design.py`

Expected: FAIL because `_layouts/research_home.html` and `_sass/_research-home.scss` do not exist yet.

- [ ] **Step 3: Implement the homepage layout and styles**

Create `_layouts/research_home.html`, update `_pages/about.md` front matter and content, create `_sass/_research-home.scss`, and import it from `assets/css/main.scss`.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 tests/test_homepage_design.py`

Expected: PASS.

### Task 2: Build And Preview

**Files:**
- Build output only: `_site/`

- [ ] **Step 1: Build the site**

Run: `bundle exec jekyll build`

Expected: the site builds without Liquid or Sass errors.

- [ ] **Step 2: Start a local server**

Run: `bundle exec jekyll serve --host 127.0.0.1 --port 4000`

Expected: homepage is available at `http://127.0.0.1:4000/`.

- [ ] **Step 3: Verify the rendered homepage**

Open the local homepage and check desktop/mobile layout, photo rendering, selected publications, news, and service.
