from plyer import notification
import time

# Sample list of English sentences to learn
english_sentences = [
    "How’s it going?",
    "What’s for dinner?",
    "What’s happening this weekend?",
    "Do you have any plans for today?",
    "Are you busy or are you free to chat?",
    "Where are my keys?",
    "What are you getting up to this weekend?",
    "Are you keen to get together on Saturday?",
    "You’re joking?",
    "Have you got much going on these days?",
    "How’s your workday looking?",
    "Should we grab a bite to eat?",
    "Would you like to grab a coffee this afternoon?",
    "Would you mind helping me quickly?",
    "What are you up to?",
    "Could you give me a lift?",
    "Can I help you with anything?",
    "What time are you getting home today?",
    "Should we eat out tonight?",
    "How does pizza sound?",
    "What do you feel like doing?",
    "What are you watching?",
    "What are you reading?",
    "Are you keen to catch a movie tonight?",
    "What are you thinking about?",
    "Have you fed the dogs?",
    "What do you want to do?",
    "What do you want to eat?",
    "Can I make you some coffee?",
    "Where are you going?",
    "Should I take the dog for a walk?",
    "How much does it cost?",
    "Do you want to meet up next week?",
    "We could do dinner on Wednesday night?",
    "What’s on your mind?",
    "What’s eating you?",
    "Do you have a minute?",
    "Is everything OK?",
    "How was your weekend?",
    "How are you feeling today?",
    "What time did you get up?",
    "What time do we need to be there?",
    "What time is your flight?",
    "You coming?"
]

if __name__ == '__main__':
    sentence_index = 0  # Initialize the index to track which sentence to display
    
    while True:
        # Display notification with the current English sentence
        notification.notify(
            title="English vocabulary",
            message=english_sentences[sentence_index],
            timeout=5
        )
        
        # Increment the index to display the next sentence in the next iteration
        sentence_index = (sentence_index + 1) % len(english_sentences)
        
        # Wait for second before displaying the next notification
        time.sleep(3600)
