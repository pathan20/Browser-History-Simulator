# ============================================================
# SHORTEST PATH TRAVEL PLANNER
# Data Structure : Graph
# Algorithm      : Dijkstra's Algorithm
# ============================================================

import heapq


class TravelPlanner:

    def __init__(self):
        # Graph represented using an adjacency list
        self.graph = {}

    # --------------------------------------------------------
    # Add a location
    # --------------------------------------------------------
    def add_location(self, location):

        if location not in self.graph:
            self.graph[location] = {}

    # --------------------------------------------------------
    # Add a road between two locations
    # --------------------------------------------------------
    def add_route(self, source, destination, distance):

        self.add_location(source)
        self.add_location(destination)

        # Since the road is bidirectional
        self.graph[source][destination] = distance
        self.graph[destination][source] = distance

    # --------------------------------------------------------
    # Display all locations and routes
    # --------------------------------------------------------
    def display_routes(self):

        print("\n" + "=" * 60)
        print("                 TRAVEL MAP")
        print("=" * 60)

        for location in sorted(self.graph):

            print(f"\n{location}:")

            if not self.graph[location]:
                print("   No connected locations")
                continue

            for destination, distance in self.graph[location].items():

                print(
                    f"   -> {destination} "
                    f"({distance:g} km)"
                )

        print("=" * 60)

    # --------------------------------------------------------
    # Dijkstra's Algorithm
    # --------------------------------------------------------
    def shortest_path(self, start, destination):

        # Check whether locations exist
        if start not in self.graph:
            return None, None

        if destination not in self.graph:
            return None, None

        # Distance from start to every location
        distances = {
            location: float("inf")
            for location in self.graph
        }

        # Previous location used to reconstruct the route
        previous = {
            location: None
            for location in self.graph
        }

        # Distance to starting location is zero
        distances[start] = 0

        # Priority queue
        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_location = heapq.heappop(
                priority_queue
            )

            # Ignore outdated queue entries
            if current_distance > distances[current_location]:
                continue

            # Destination reached
            if current_location == destination:
                break

            # Check all neighboring locations
            for neighbor, distance in self.graph[
                current_location
            ].items():

                new_distance = (
                    current_distance + distance
                )

                # Found a shorter route
                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance

                    previous[neighbor] = current_location

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        # No route exists
        if distances[destination] == float("inf"):
            return None, None

        # ----------------------------------------------------
        # Reconstruct shortest path
        # ----------------------------------------------------

        path = []

        current = destination

        while current is not None:

            path.append(current)

            current = previous[current]

        # Reverse the path
        path.reverse()

        return path, distances[destination]


# ============================================================
# Add Sample Locations
# ============================================================

def create_sample_map(planner):

    routes = [

        ("Pune", "Mumbai", 150),

        ("Pune", "Nashik", 210),

        ("Pune", "Satara", 120),

        ("Mumbai", "Nashik", 165),

        ("Mumbai", "Surat", 285),

        ("Nashik", "Surat", 310),

        ("Satara", "Kolhapur", 120),

        ("Kolhapur", "Goa", 230),

        ("Goa", "Mangalore", 360),

        ("Surat", "Ahmedabad", 265)

    ]

    for source, destination, distance in routes:

        planner.add_route(
            source,
            destination,
            distance
        )


# ============================================================
# Find Shortest Route
# ============================================================

def find_route(planner):

    print("\n--- FIND SHORTEST ROUTE ---")

    start = input(
        "Enter starting location: "
    ).strip()

    destination = input(
        "Enter destination: "
    ).strip()

    path, distance = planner.shortest_path(
        start,
        destination
    )

    if path is None:

        print("\nNo route found.")

        print(
            "\nPlease check the location names."
        )

        return

    print("\n" + "=" * 60)

    print("              SHORTEST ROUTE")

    print("=" * 60)

    print(
        "\nRoute:"
    )

    print(
        " -> ".join(path)
    )

    print(
        f"\nTotal Distance: {distance:g} km"
    )

    print(
        f"Number of Stops: {len(path) - 1}"
    )

    print("=" * 60)


# ============================================================
# Add New Route
# ============================================================

def add_new_route(planner):

    print("\n--- ADD NEW ROUTE ---")

    source = input(
        "Enter source location: "
    ).strip()

    destination = input(
        "Enter destination location: "
    ).strip()

    try:

        distance = float(
            input("Enter distance in km: ")
        )

        if distance <= 0:

            print(
                "\nDistance must be greater than 0."
            )

            return

        planner.add_route(
            source,
            destination,
            distance
        )

        print(
            "\nRoute added successfully!"
        )

    except ValueError:

        print(
            "\nPlease enter a valid number."
        )


# ============================================================
# Main Program
# ============================================================

def main():

    planner = TravelPlanner()

    # Create initial map
    create_sample_map(planner)

    while True:

        print("\n")

        print("=" * 60)

        print(
            "             SHORTEST PATH TRAVEL PLANNER"
        )

        print("=" * 60)

        print("1. Find Shortest Route")

        print("2. Display Travel Map")

        print("3. Add New Route")

        print("4. Display Locations")

        print("5. Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Find shortest route
        # ----------------------------------------------------

        if choice == "1":

            find_route(planner)

        # ----------------------------------------------------
        # Display map
        # ----------------------------------------------------

        elif choice == "2":

            planner.display_routes()

        # ----------------------------------------------------
        # Add route
        # ----------------------------------------------------

        elif choice == "3":

            add_new_route(planner)

        # ----------------------------------------------------
        # Display locations
        # ----------------------------------------------------

        elif choice == "4":

            print("\nAvailable Locations:")

            for location in sorted(
                planner.graph
            ):

                print(
                    " -", location
                )

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "5":

            print(
                "\nThank you for using "
                "Shortest Path Travel Planner!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter 1-5."
            )


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":

    main()