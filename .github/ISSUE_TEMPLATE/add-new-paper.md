---
name: Add new paper
about: Fill in the form to add a new paper to the catalog
title: ''
labels: ''
assignees: ''

---

name: "Add new paper"
description: "Form to add a new entry on the catalog"
body:
  - type: markdown
    attributes:
      value: |
        Fill in the details of the paper and provide a brief description of the most interesting aspects of it
  - type: input
    id: paper-title
    attributes:
      label: "Paper's Title:"
      description: "Title"
    validations:
      required: true
  - type: input
    id: paper-year-of-pub
    attributes:
      label: "Paper's Publication Year:"
      description: "Year of Publication"
    validations:
      required: true
  - type: textarea
    id: tldr
    attributes:
      label: "TL;DR"
      description: "Give an overview of the main aspects of this paper in your own words"
      placeholder: "Write down all the details that caught your attention!"
    validations:
      required: true
  - type: input
    id: paper-link
    attributes:
      label: "Link to the Publication:"
      description: "A link that redirects to the publication (when available and when under the publication's license permission)"
    validations:
      required: false
