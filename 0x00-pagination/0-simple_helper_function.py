#!/usr/bin/env python3
""" Calculates the start and end indexes """


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
