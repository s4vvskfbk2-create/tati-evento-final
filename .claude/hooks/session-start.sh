#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install Python dependencies for Excel and PDF generation (skill: orcamento-eventos-nobre)
pip install --quiet openpyxl weasyprint
