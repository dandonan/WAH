
states = {
    STARTMODE: '_STARTMODE',               # Prompt the user to start asking questions
    ASKMODE: '_ASKMODE',                   # Alexa is asking user the questions.
    DESCRIPTIONMODE: '_DESCRIPTIONMODE'     # Alexa is describing the final choice and prompting to ask another question or leave
};
question  = [
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
        """{ "question": "" , "message": "" },
          { "question": "" , "message": "" },
          { "question": "" , "message": "" },
          { "question": "" , "message": "" },
        """

welcomeMessage = "Welcome to Women Access Health or W A H";
repeatWelcomeMessage = "What would you like to know";
repeatMessage = "Say 'tell me more' or 'Repeat'";
goodbyeMessage = "Goodbye Hope I helped!";
couldNotUnderstand = "I'm sorry, I could not understand you";
helpMessage = "I can assist you with any womanly needs you may have";
promptToStartMessage = "Is there anything I can help you with";
promptToContinueMessage = "Is there anything I can help you with";
#starting and setting up
Alexa = require("alexa-sdk");
APP_ID = Unset;

exports.handler = def (event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.appId = APP_ID;
    alexa.resources = languageString;
    alexa.registerHandlers(newSessionHandlers, startGameHandlers,  askQuestionHandlers);
    alexa.execute();
};
var newSessionHandler = {
  'LaunchRequest': def () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
  },
  'AMAZON.HelpIntent': def () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', helpMessage, helpMessage);
  },
  'Unhandled': def () {
    this.handler.state = states.STARTMODE;
    this.emit(':ask', promptToStartMessage, promptToStartMessage);
  }
};
var startGameHandlers = Alexa.CreateStateHandler(states.STARTMODE, {
    'AMAZON.YesIntent': def () {

        this.handler.state = states.ASKMODE;

        var message = helper.getSpeechForNode(START_NODE);
        this.emit(':ask', message, message);
    },
    'AMAZON.StopIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.HelpIntent': def () {
        this.emit(':ask', helpMessage, helpMessage);
    },
    'Unhandled': def () {
        this.emit(':ask', promptToStartMessage, promptToStartMessage);
    }
});
var askQuestionHandlers = Alexa.CreateStateHandler(states.ASKMODE, {
    'AMAZON.YesIntent': def () {

        helper.question(this,':ask');

    },
    'AMAZON.HelpIntent': def () {
        this.emit(':ask', helpMessage, helpMessage);
    },
    'AMAZON.StopIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StartOverIntent': def () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'Unhandled': def () {
        this.emit(':ask', promptToContinueMessage, promptToContinueMessage);
    }
});
/*var descriptionHandlers = Alexa.CreateStateHandler(states.DESCRIPTIONMODE{
 'AMAZON.YesIntent': def () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'AMAZON.NoIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StopIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.CancelIntent': def () {
        this.emit(':tell', goodbyeMessage);
    },
    'AMAZON.StartOverIntent': def () {
        this.handler.state = states.STARTMODE;
        this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
    },
    'Unhandled': def () {
        this.emit(':ask', promptToContinueMessage, promptToContinueMessage);
    }
});
*/
