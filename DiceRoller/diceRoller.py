import random

def roll_dice(num_roll):
    dice = [[" ------- ","|       |","|   *   |","|       |"," ------- "],
            [" ------- ","|     * |","|       |","| *     |"," ------- "],
            [" ------- ","|     * |","|   *   |","| *     |"," ------- "],
            [" ------- ","| *   * |","|       |","| *   * |"," ------- "],
            [" ------- ","| *   * |","|   *   |","| *   * |"," ------- "]]

    while(1 <= num_roll):

        x = random.randrange(5)
        y = random.randrange(5)
        print("\n")

        for i in range(5):
            print(dice[x][i],dice[y][i])
        num_roll -= 1




