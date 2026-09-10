def main():
    """
    Runs the cinema ticket pre-sale program and keeps track of
    tickets sold and the total number of buyers.

    Parameters:
        None

    Variables:
        total_tickets (int): The total number of tickets available.
       Total_buyers (int): Keeps track of the total number of buyers.
        tickets (int): The number of tickets purchased by each buyer.

    Logic:
        1. Set the total number of available tickets to 10.
        2. Set the number of buyers to 0.
        3. Display the number of tickets remaining.
        4. Ask the buyer to purchase between 1 and 4 tickets.
        5. Check that the number entered is valid.
        6. Subtract the purchased tickets from the total.
        7. Add one to the number of buyers.
        8. Continue until all 20 tickets have been sold.
        9. Display the total number of buyers.

    Return:
        None
    """

    total_tickets = 10
    total_buyers = 0

    print("Cinema Ticket Pre-Sale")
    print("----------------------")

    while total_tickets > 0:
        print("\nTickets remaining:", total_tickets)

        tickets_wanted = int(input("How many cinema tickets would you like to purchase? "))

        while tickets < 1 or tickets > 4 or tickets > total_tickets:
            print("Invalid number of tickets.")
            tickets = int(input("How many tickets would you like to buy (1-4)? "))

        total_tickets -= tickets
     Total_buyers += 1

    print("\nAll tickets have been sold!")
    print("Total number of buyers:", buyers)


if __name__ == "__main__":
    main()
