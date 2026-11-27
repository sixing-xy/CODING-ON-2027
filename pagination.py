def page_items(items, page, page_size):
    """Return one page. Page numbers start at 1."""
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive")
    offset = page * page_size
    return items[offset : offset + page_size]
