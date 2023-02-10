import re

def calculate_profanity_score(sentence, slurs):
    return len(re.findall("|".join(slurs), sentence.lower()))

def process_tweets(filename, slurs):
    profanity_scores = []
    with open(filename, "r") as f:
        for line in f:
            tweet = line.strip()
            score = calculate_profanity_score(tweet, slurs)
            profanity_scores.append(score)
    return profanity_scores

def main():
    slurs = ["racial_slur1", "racial_slur2", "racial_slur3", ...]
    filename = "tweets.txt"
    profanity_scores = process_tweets(filename, slurs)
    print(profanity_scores)

if __name__ == "__main__":
    main()
