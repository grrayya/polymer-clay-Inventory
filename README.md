# polymer-clay-Inventory
Inventory Manager 

Python-based terminal-based Command Line Interface (CLI) program for managing local item inventories.

Features
Stock counts are saved and loaded locally using JSON for persistent data storage.
Easily add new product listings (such as Glazed Penguin Charms), change stock following sales, or remove discontinued items with the full CRUD functionality.
Rich Terminal User Interface: renders a clear, color-coded table interface using the `rich` library. Restock alerts are automatically displayed in red for low-stock goods (quantity ≤ 5).

 How to Run
have the required dependencies installed:
   ```bash
   pip install rich
