from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def assert_contains(text, *needles):
    missing = [needle for needle in needles if needle not in text]
    assert not missing, "Missing expected content: " + ", ".join(missing)


def test_homepage_uses_dedicated_research_layout():
    about = read("_pages/about.md")

    assert_contains(
        about,
        "layout: research_home",
        "author_profile: false",
        'permalink: /',
    )


def test_research_home_layout_exposes_required_sections():
    layout = read("_layouts/research_home.html")

    assert_contains(
        layout,
        'class="research-home"',
        'class="research-home__rail"',
        'class="research-home__portrait"',
        'alt="Jiongli Zhu"',
        'class="research-home__bio"',
        'id="publications"',
        'id="news"',
        'id="service"',
        "site.publications",
        "limit: 3",
        "page.service_summary",
    )
    assert "research-home__service-list" not in layout


def test_publications_page_uses_constructed_layout():
    page = read("_pages/publications.md")
    layout = read("_layouts/research_publications.html")

    assert_contains(
        page,
        "layout: research_publications",
        "author_profile: false",
        "permalink: /publications/",
    )
    assert_contains(
        layout,
        'class="research-publications"',
        "site.publications",
        "sort: \"date\"",
        'class="research-publications__item"',
        'class="research-publications__meta"',
    )


def test_publication_details_use_constructed_layout():
    config = read("_config.yml")
    layout = read("_layouts/research_publication.html")

    assert_contains(
        config,
        "type: publications",
        "layout: research_publication",
        "author_profile: false",
    )
    assert_contains(
        layout,
        'class="research-publication"',
        'class="research-publication__header"',
        'class="research-publication__authors"',
        'class="research-publication__actions"',
        'class="research-publication__abstract"',
        "page.paperurl",
    )


def test_footer_has_no_legacy_follow_or_sitemap_clutter():
    footer = read("_includes/footer.html")
    custom_footer = read("_includes/footer/custom.html")
    head = read("_includes/head.html")

    assert "page__footer-follow" not in footer
    assert "social-icons" not in footer
    assert "Feed" not in footer
    assert "AcademicPages" not in footer
    assert "Minimal Mistakes" not in footer
    assert "Sitemap" not in custom_footer
    assert "feed.xml" not in head


def test_jekyll_excludes_non_site_source_directories():
    config = read("_config.yml")

    assert_contains(
        config,
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "docs",
        "tests",
        "markdown_generator",
        "talkmap",
        "talkmap.py",
        "talkmap.ipynb",
    )


def test_only_active_profile_image_remains():
    image_files = sorted(path.name for path in (ROOT / "images").iterdir() if path.is_file())
    assert image_files == ["profile.jpeg"]


def test_mint_publication_is_present():
    mint = read("_publications/mint26.md")

    assert_contains(
        mint,
        'title: "MINT: Multi-Vector Search Index Tuning."',
        "venue: 'ICDE'",
        "date: 2026-01-01",
        "Jiongli Zhu",
        "Yue Wang",
        "Bailu Ding",
        "Philip A. Bernstein",
        "Vivek Narasayya",
        "Surajit Chaudhuri",
        "https://arxiv.org/abs/2504.20018",
    )


def test_legacy_archive_and_sample_sources_removed():
    removed_paths = [
        "_pages/archive-layout-with-content.md",
        "_pages/category-archive.html",
        "_pages/collection-archive.html",
        "_pages/markdown.md",
        "_pages/non-menu-page.md",
        "_pages/page-archive.html",
        "_pages/portfolio.html",
        "_pages/sitemap.md",
        "_pages/tag-archive.html",
        "_pages/talkmap.html",
        "_pages/talks.html",
        "_pages/teaching.html",
        "_pages/terms.md",
        "_pages/year-archive.html",
        "_posts/2012-08-14-blog-post-1.md",
        "_posts/2013-08-14-blog-post-2.md",
        "_posts/2014-08-14-blog-post-3.md",
        "_posts/2015-08-14-blog-post-4.md",
        "_posts/2199-01-01-future-post.md",
        "_portfolio/portfolio-1.md",
        "_portfolio/portfolio-2.html",
        "_talks/2012-03-01-talk-1.md",
        "_talks/2013-03-01-tutorial-1.md",
        "_talks/2014-02-01-talk-2.md",
        "_talks/2014-03-01-talk-3.md",
        "_teaching/2014-spring-teaching-1.md",
        "_teaching/2015-spring-teaching-2.md",
    ]

    existing = [path for path in removed_paths if (ROOT / path).exists()]
    assert not existing, "Legacy archive/sample sources still present: " + ", ".join(existing)


def test_homepage_styles_are_imported_and_responsive():
    main_scss = read("assets/css/main.scss")
    home_scss = read("_sass/_research-home.scss")

    assert '@import "research-home";' in main_scss
    assert_contains(
        home_scss,
        ".research-home",
        ".greedy-nav",
        "button {",
        "grid-template-columns",
        "@media",
        "max-width",
        "minmax(0, 1fr)",
    )


if __name__ == "__main__":
    test_homepage_uses_dedicated_research_layout()
    test_research_home_layout_exposes_required_sections()
    test_publications_page_uses_constructed_layout()
    test_publication_details_use_constructed_layout()
    test_footer_has_no_legacy_follow_or_sitemap_clutter()
    test_mint_publication_is_present()
    test_jekyll_excludes_non_site_source_directories()
    test_only_active_profile_image_remains()
    test_legacy_archive_and_sample_sources_removed()
    test_homepage_styles_are_imported_and_responsive()
    print("homepage design checks passed")
