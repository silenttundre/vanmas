#!/usr/bin/env python
import sys
from van_mas_proj.crew import MyMasCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "Product_Category": "Cereal",  # Consumer input about product category
        "Target_Brands": "Honey Bunches of Oats, Kellogg's",  # Initial list of products to consider
        "Key_Features": "Low in sugar, No artificial colors or flavors, No preservatives"  # Specific consumer requirements and desired features
    }
    MyMasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "Product_Category": "Cereal",  # Consumer input about product category
        "Target_Brands": "Honey Bunches of Oats, Kellogg's",  # Initial list of products to consider
        "Key_Features": "Low in sugar, No artificial colors or flavors, No preservatives"  # Specific consumer requirements and desired features
    }
    try:
        MyMasCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMasCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "Product_Category": "Cereal",  # Consumer input about product category
        "Target_Brands": "Honey Bunches of Oats, Kellogg's",  # Initial list of products to consider
        "Key_Features": "Low in sugar, No artificial colors or flavors, No preservatives"  # Specific consumer requirements and desired features
    }
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
