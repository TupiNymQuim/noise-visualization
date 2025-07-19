import pygame
import sys
import concurrent.futures

import graphics
import packets


def main():
    if len(sys.argv) == 3:
        script_path = sys.argv[1]
        interface = sys.argv[2]
    else:
        script_path = input("Enter the monitoring script path: ")
        interface = input("Enter the network interface to monitor: ")

    circles = []

    pygame.init()
    screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
    pygame.display.set_caption("VPN Demo")
    clock = pygame.time.Clock()
    running = True

    try:
        pc_image = pygame.image.load('pc.png')
        optimized_pc = pc_image.convert_alpha()
        scaled_pc = pygame.transform.scale(
            optimized_pc, (600, 850))
        pc_rect = scaled_pc.get_rect()
        pc_rect.center = (72, 200)

    except pygame.error as e:
        print(f"Error loading images: {e}")
        pygame.quit()
        return

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(packets.get_packets, script_path, interface)
        latest_packets_time = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            graphics.animate_packets(circles, screen, scaled_pc, pc_rect)

            if (pygame.time.get_ticks() - latest_packets_time > 1500):
                packet_sizes = future.result()
                scaled_packet_sizes = packets.scale_numbers(packet_sizes)
                graphics.add_packets(scaled_packet_sizes, circles)
                future = executor.submit(
                    packets.get_packets, script_path, interface)
                latest_packets_time = pygame.time.get_ticks()

            clock.tick(60)  # Limit to 60 frames per second

        pygame.quit()


if __name__ == "__main__":
    main()
