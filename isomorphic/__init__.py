def run(in_colab):
    env_string = "local"
    if in_colab:
        env_string = "Google colab"
    print("You're up and running in a {} environment!".format(env_string))
