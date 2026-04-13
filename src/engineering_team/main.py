#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime


from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A perishable inventory system for a small food retail or meal-prep operation (single store, in-memory).
Stock is tracked in batches: each batch has a SKU, quantity received, received date, expiry date, and unit cost at receipt.
The system should allow receiving new stock (creating a batch), selling to customers (reducing quantity), and recording waste/spoilage
(reducing quantity with a reason). When fulfilling sales or waste, allocate quantity across batches using a clear, documented policy
(e.g. FIFO by expiry or receipt—pick one and apply it consistently).
The system should refuse to sell or waste more units than are available for a SKU, and should not sell units that are already expired
at the time of the sale (define "current time" as a single configurable "as of" date for the demo if that simplifies testing).
The system has access to a function get_retail_price(sku) that returns the shelf price per unit for a SKU; include a test stub that
returns fixed prices for a small set of SKUs (e.g. MILK_1L, SALAD_BOX, SOUP_PINT).
The system should report on-hand quantity per SKU, batches with quantities and expiry dates, total inventory value at cost,
estimated retail value using get_retail_price, spoilage/waste totals, and simple margin indicators (revenue minus cost of goods for sales).
The system should list a chronological ledger of operations (receipts, sales, waste) with enough detail to audit changes.
The system should support reporting "expiring soon" (e.g. within N days of the as-of date) and basic low-stock signals if you define thresholds.
"""
module_name = "inventory.py"
class_name = "Inventory"


def run():
    """
    Run the engineering crew (design, UX, implementation, UI, QA).
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()