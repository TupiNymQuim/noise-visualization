import graphics
import packets
import pygame
import concurrent.futures

# import time


def main():
    circles = []

    pygame.init()
    screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
    pygame.display.set_caption("Animated Circles")
    clock = pygame.time.Clock()
    running = True

    # coroutine = asyncio.to_thread(packets.get_packets())
    # test = await coroutine
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(packets.get_packets)
        latest_packets_time = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            graphics.animate_packets(circles, screen)

            if (pygame.time.get_ticks() - latest_packets_time > 1500):
                packet_sizes = future.result()
                scaled_packet_sizes = packets.scale_numbers(packet_sizes)
                graphics.add_packets(scaled_packet_sizes, circles)
                future = executor.submit(packets.get_packets)
                latest_packets_time = pygame.time.get_ticks()

            clock.tick(60)  # Limit to 60 frames per second

        pygame.quit()


if __name__ == "__main__":
    main()
