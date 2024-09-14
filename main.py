import time
from rules import BirthRule, StayAliveRule, LonelyDeathRule, OverPopulateRule
from forest_fire_rules import TreeBurnRule, BurnedTreeToTree, BurnTreeToBurned
from game import Game, GameFire
from visualizer import visualize
    


def main():
    config = {
        "rows": 60,
        "cols": 60,
        "generations": 120,
        # "rules": [BirthRule, StayAliveRule, LonelyDeathRule, OverPopulateRule],
        "rules": [TreeBurnRule, BurnTreeToBurned],
        "density": 0.45,
        "sleep_time": 0.2,
        "output_type": "visualizer"
    }

    # game = Game(config["rows"], config["cols"], config["rules"])
    game = GameFire(config["rows"], config['cols'], config['rules'], config["density"])


    if config["output_type"] == "visualizer":

        visualize(game, config["generations"], config["sleep_time"])

    elif config["output_type"] == "console":
        for generation in range(1, config["generations"] + 1):
            game.update()
            print(f"Generation {generation}:\n")
            print(game.grid)
            time.sleep(config["sleep_time"])

if __name__ == "__main__":
    main()

            