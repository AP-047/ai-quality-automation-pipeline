# AI Quality Automation Pipeline for Engineering Deliverables

## Brief Description

A rule-based and AI-assisted automation system for validating engineering deliverables.
The system performs structured quality checks, generates validation reports and integrates with workflow automation tools for scalable execution.

## Problem Statement

In engineering environments, release readiness depends on consistent validation of deliverables such as specifications, reports and design artifacts.
Manual validation is time-consuming, error-prone and not scalable.

This project simulates a quality automation system that replaces manual checks with structured, repeatable validation workflows.

## Key Features

- Rule-based validation using configurable YAML rules
- Automated checks for completeness, naming conventions and status consistency
- Structured report generation with summary metrics
- REST API built with FastAPI for integration
- Workflow orchestration using n8n
- AI-assisted summarization using a local LLM (Ollama)

## Architecture Overview

Data -> Validation Engine -> Report Generator -> AI Summary -> API -> n8n Workflow

## Tech Stack

- Python
- FastAPI
- n8n
- YAML / JSON
- Ollama (local LLM - gemma:2b)
- Requests (API integration)

## How It Works

- Input data simulates engineering deliverables
- YAML rules define validation logic
- Validation engine applies rule-based checks
- Results are aggregated into a structured report
- AI layer generates a concise summary
- API exposes the pipeline
- n8n orchestrates workflow execution

## Example Output

The system generates:

- total items
- pass/fail counts
- validation errors per item
- AI-generated summary

## Why This Project

This project demonstrates how quality validation in engineering workflows can be automated using a combination of deterministic rules and AI-based insights.

## Future Improvements

- Integration with real data sources (e.g., Jira, PLM systems)
- Advanced rule engine with dynamic configurations
- Dashboard for visualization
- Scalable deployment using containers