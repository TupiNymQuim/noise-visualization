import subprocess


def get_packets():
    script_path = [
        "/home/gcorreia/projects/nym/noise-visualization/monitor.sh"]
    result = subprocess.run(script_path, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    numbers = [int(line) for line in output.splitlines()]
    return numbers


def scale_numbers(numbers):
    """
    Scales a list of numbers from the range [50, 5000] to [10, 300].

    Args:
        numbers: A list of numbers within the range [50, 5000].

    Returns:
        A new list with the numbers scaled to the range [10, 300].
    """

    if not numbers:
        return []  # Return an empty list if the input list is empty

    min_input = 30
    max_input = 1500
    min_output = 5
    max_output = 100

    scaled_numbers = []
    for num in numbers:
        if not (min_input <= num <= max_input):
            raise ValueError(
                f"Number {num} is outside the allowed range [50, 5000].")

        # Linear scaling formula
        scaled_num = int((num - min_input) / (max_input - min_input) *
                         (max_output - min_output) + min_output)
        scaled_numbers.append(scaled_num)

    return scaled_numbers
