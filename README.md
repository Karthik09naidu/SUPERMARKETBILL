Shopping Bill Generator

This project is a Python-based shopping bill generator that allows users to simulate a simple shopping experience by selecting items, entering quantities, and generating a detailed bill. It includes features such as GST calculation and a formatted bill summary.

Features

Interactive Console Interface: Users can select items from a predefined list and specify quantities.

Itemized Bill: The bill displays details like item names, quantities, and individual prices.

GST Calculation: A 5% GST is added to the total price.

Final Amount Display: The total cost, including GST, is shown.

Exit Option: Users can exit the shopping process at any time.

Prerequisites

Python 3.x installed on your system.

How to Run

Clone this repository or download the Python script.

Open the terminal or command prompt.

Navigate to the directory containing the script.

Run the script using the command:

python shopping_bill_generator.py

Follow the on-screen prompts to:

View the list of available items.

Select items and enter quantities.

Generate and view the final bill.

Items Available

The following items are available for purchase:

Item

Price

Rice

Rs 20/Kg

Sugar

Rs 40/Kg

Salt

Rs 12/Kg

Oil

Rs 140/L

Paneer

Rs 150/Kg

Maggie

Rs 80/Kg

Milk

Rs 60/L

Curd

Rs 80/Kg

Colgate

Rs 110/250G

Example Output

An example of the bill generated:

Name: K.KARTHIK                        Date: 2024-12-12 12:34:56.789123
-----------------------------------------------------------------------
sno        items        quantity        price
-----------------------------------------------------------------------
1          Rice         2              Rs 40
2          Sugar        1              Rs 40
-----------------------------------------------------------------------
                                      Total Amount: Rs 80
                                      GST Amount:   Rs 4
-----------------------------------------------------------------------
                                      Final Amount: Rs 84
-----------------------------------------------------------------------

=================================== Dmart =============================
================================ Miryalaguda ==========================
                             Thanking You For Visit
                             

Notes

Ensure you enter valid item names when prompted.

Enter 2 to exit the shopping process when prompted.

Only items listed in the predefined inventory can be purchased.

Future Improvements

Adding the ability to save bills to a file.

Allowing dynamic item addition by store administrators.

Creating a graphical user interface (GUI).

Adding support for discounts and promotional offers.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

