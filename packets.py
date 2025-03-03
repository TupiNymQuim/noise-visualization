import subprocess


def get_packets(script_path, interface):
    result = subprocess.run([script_path, interface], stdout=subprocess.PIPE)
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
        return []

    min_input = 30
    max_input = 1500
    min_output = 2
    max_output = 50

    scaled_numbers = []
    for num in numbers:
        if (num < min_input):
            num = min_input
        elif (num > max_input):
            num = max_input

        # Linear scaling formula
        scaled_num = int((num - min_input) / (max_input - min_input) *
                         (max_output - min_output) + min_output)
        scaled_numbers.append(scaled_num)

    return scaled_numbers
