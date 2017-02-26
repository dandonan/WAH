
var states = {
    STARTMODE: '_STARTMODE',               // Prompt the user to start asking questions
    ASKMODE: '_ASKMODE',                   // Alexa is asking user the questions.
    DESCRIPTIONMODE: '_DESCRIPTIONMODE'     // Alexa is describing the final choice and prompting to ask another question or leave
};
var question  = [
        { "question": "What do i do as a victim", "message": "You should reach out and talk with someone who's there to help you in a supporting environment. Here are some resource centers near to you" },
        { "question": "I've been sexually assaulted and need help", "message": "Recognizing that there is a problem is the first stage of getting help. The best course of action is to talk to someone you can trust. I've found" },
        { "question": "My boyfriend/husband hit me what do i do", "message": "It's important to talk to someone who's there to help you about this. I've found" },
        { "question": "Can your find me a center for domestic abuse", "message": "Absolutely. Here's what I found" },             
        { "question": "What is Domestic Violence", "message": "Domestic Violence is violent or aggressive behavior within the home, typically involving the violent abuse of a spouse or partner" },
        { "question": "What is the Law against Domestic Violence", "message": "In Colorado, domestic violence is defined as any crime committed as a means of coercion, control, punishment, intimidation, or revenge against an intimate partner, not only an act of violence. If officers are called out and they have probable cause to believe someone committed an act of Domestic Violence, the suspect of the crime must be arrested. Under the Colorado Constitution, some crimes are considered victims' rights cases. By definition, all Domestic Violence crimes are victim's rights cases. This means that the victim has several rights, including the right to consult with the DA before any offers are made and when bond is addressed. They have the right to speak at sentencing and to be notified when an incarcerated defendant will be released" },
        { "question": "Can you find me a question", "message": "Sure. What kind of question do you need? There are domestic abuse, empowerment, sexual abuse planned parent hood and general womens questions. Which would you like", "domestic abuse": 1, "empowerment": 2, "sexual abuse": 3, "planned parent hood": 4,  "general womens support": 5 },
        { "question": 1, "message": "" },
        { "question": 2, "message": "" },
        { "question": 3, "message": "" },
        { "question": 4, "message": "" },
        { "question": 5, "message": "" }
    ];
        /*{ "question": "" , "message": "" },
          { "question": "" , "message": "" },
          { "question": "" , "message": "" },
          { "question": "" , "message": "" },
        */
             
var welcomeMessage = "Welcome to Women Access Health or W A H";
var repeatWelcomeMessage = "What would you like to know";
var repeatMessage = "Say 'tell me more' or 'Repeat'";
var goodbyeMessage = "Goodbye Hope I helped!";
var couldNotUnderstand = "I'm sorry, I could not understand you";
var helpMessage = "I can assist you with any womanly needs you may have";
var promptToStartMessage = "Is there anything I can help you with";
var promptToContinueMessage = "Is there anything I can help you with";

var languageString = {
    "en-GB": {
        "translation": {
            "QUESTIONS" : questions["QUESTIONS_EN_GB"],
            "GAME_NAME" : "British Reindeer Trivia", // Be sure to change this for your skill.
            "HELP_MESSAGE": "I will ask you %s multiple choice questions. Respond with the number of the answer. " +
            "For example, say one, two, three, or four. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": "Would you like to start playing?",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Would you like to keep playing?",
            "CANCEL_MESSAGE": "Ok, let\'s play again soon.",
            "NO_MESSAGE": "Ok, we\'ll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to %s. ",
            "WELCOME_MESSAGE": "I will ask you %s questions, try to get as many right as you can. " +
            "Just say the number of the answer. Let\'s begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is %s: %s. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question %s. %s ",
            "GAME_OVER_MESSAGE": "You got %s out of %s questions correct. Thank you for playing!",
            "SCORE_IS_MESSAGE": "Your score is %s. "
        }
    },
    "en-US": {
        "translation": {
            "QUESTIONS" : questions["QUESTIONS_EN_US"],
            "GAME_NAME" : "American Reindeer Trivia", // Be sure to change this for your skill.
            "HELP_MESSAGE": "I will ask you %s multiple choice questions. Respond with the number of the answer. " +
            "For example, say one, two, three, or four. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": "Would you like to start playing?",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Would you like to keep playing?",
            "CANCEL_MESSAGE": "Ok, let\'s play again soon.",
            "NO_MESSAGE": "Ok, we\'ll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to %s. ",
            "WELCOME_MESSAGE": "I will ask you %s questions, try to get as many right as you can. " +
            "Just say the number of the answer. Let\'s begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is %s: %s. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question %s. %s ",
            "GAME_OVER_MESSAGE": "You got %s out of %s questions correct. Thank you for playing!",
            "SCORE_IS_MESSAGE": "Your score is %s. "
        }
    },
    "de-DE": {
        "translation": {
            "QUESTIONS" : questions["QUESTIONS_DE_DE"],
            "GAME_NAME" : "Wissenswertes über Rentiere in Deutsch", // Be sure to change this for your skill.
            "HELP_MESSAGE": "Ich stelle dir %s Multiple-Choice-Fragen. Antworte mit der Zahl, die zur richtigen Antwort gehört. " +
            "Sage beispielsweise eins, zwei, drei oder vier. Du kannst jederzeit ein neues Spiel beginnen, sage einfach „Spiel starten“. ",
            "REPEAT_QUESTION_MESSAGE": "Wenn die letzte Frage wiederholt werden soll, sage „Wiederholen“ ",
            "ASK_MESSAGE_START": "Möchten Sie beginnen?",
            "HELP_REPROMPT": "Wenn du eine Frage beantworten willst, antworte mit der Zahl, die zur richtigen Antwort gehört. ",
            "STOP_MESSAGE": "Möchtest du weiterspielen?",
            "CANCEL_MESSAGE": "OK, dann lass uns bald mal wieder spielen.",
            "NO_MESSAGE": "OK, spielen wir ein andermal. Auf Wiedersehen!",
            "TRIVIA_UNHANDLED": "Sagt eine Zahl beispielsweise zwischen 1 und %s",
            "HELP_UNHANDLED": "Sage ja, um fortzufahren, oder nein, um das Spiel zu beenden.",
            "START_UNHANDLED": "Du kannst jederzeit ein neues Spiel beginnen, sage einfach „Spiel starten“.",
            "NEW_GAME_MESSAGE": "Willkommen bei %s. ",
            "WELCOME_MESSAGE": "Ich stelle dir %s Fragen und du versuchst, so viele wie möglich richtig zu beantworten. " +
            "Sage einfach die Zahl, die zur richtigen Antwort passt. Fangen wir an. ",
            "ANSWER_CORRECT_MESSAGE": "Richtig. ",
            "ANSWER_WRONG_MESSAGE": "Falsch. ",
            "CORRECT_ANSWER_MESSAGE": "Die richtige Antwort ist %s: %s. ",
            "ANSWER_IS_MESSAGE": "Diese Antwort ist ",
            "TELL_QUESTION_MESSAGE": "Frage %s. %s ",
            "GAME_OVER_MESSAGE": "Du hast %s von %s richtig beantwortet. Danke fürs Mitspielen!",
            "SCORE_IS_MESSAGE": "Dein Ergebnis ist %s. "
        }
    }
};

//starting and setting up


var Alexa = require("alexa-sdk"); 

exports.handler = function (event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.resources = languageString;
    alexa.registerHandlers(newSessionHandlers, startGameHandlers,  askQuestionHandlers);
    alexa.execute();
};
var newSessionHandler = {
  'LaunchRequest': function () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
  },
  'AMAZON.HelpIntent': function () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', helpMessage, helpMessage);
  },
  'Unhandled': function () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', promptToStartMessage, promptToStartMessage);
  }
};
var startGameHandlers = Alexa.CreateStateHandler(states.STARTMODE, {
    'AMAZON.YesIntent': function () {
        
        this.handler.state = states.ASKMODE;
        
        var message = helper.getSpeechForNode(START_NODE);
        this.emit(':ask', message, message);
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.HelpIntent': function () {
        this.emit(':ask', helpMessage, helpMessage);
    },
    'Unhandled': function () {
        this.emit(':ask', promptToStartMessage, promptToStartMessage);
    }
});
var askQuestionHandlers = Alexa.CreateStateHandler(states.ASKMODE, {
    'AMAZON.YesIntent': function () {
 
        helper.question(this,':ask');
    
    },
    'AMAZON.HelpIntent': function () {
        this.emit(':ask', helpMessage, helpMessage);
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StartOverIntent': function () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'Unhandled': function () {
        this.emit(':ask', promptToContinueMessage, promptToContinueMessage);
    }
});
/*var descriptionHandlers = Alexa.CreateStateHandler(states.DESCRIPTIONMODE{
 'AMAZON.YesIntent': function () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'AMAZON.NoIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StartOverIntent': function () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'Unhandled': function () {
        this.emit(':ask', promptToContinueMessage, promptToContinueMessage);
    }
});
*/