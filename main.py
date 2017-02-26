from __future__ import print_function
import json
import requests
import random

def lambda_handler(event, context):
	""" Route the incoming request based on type (LaunchRequest, IntentRequest,
	etc.) The JSON body of the request is provided in the event parameter.
	"""
	
	print("event.session.application.applicationId=" + event['session']['application']['applicationId'])
	
	"""
	Uncomment this if statement and populate with your skill's application ID to
	prevent someone else from configuring a skill that sends requests to this
	function.
	"""
	if (event['session']['application']['applicationId'] !=
			"amzn1.ask.skill.f92537cb-05a7-4e82-9afe-37f8255f46fa"):
		raise ValueError("Invalid Application ID")

	if event['session']['new']:
		on_session_started({'requestId': event['request']['requestId']},
						   event['session'])

	if event['request']['type'] == "LaunchRequest":
		return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
		return on_intent(event['request'], event['session'])
	elif event['request']['type'] == "SessionEndedRequest":
		return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
	""" Called when the session starts """

	session_attributes = {}
	print("on_session_started requestId=" + session_started_request['requestId']
		  + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
	""" Called when the user launches the skill without specifying what they
	want
	"""

	print("on_launch requestId=" + launch_request['requestId'] +
		  ", sessionId=" + session['sessionId'])
	# Dispatch to your skill's launch
	return get_welcome_response()

def on_intent(intent_request, session):
	print("on_intent requestId=" + intent_request['requestId'] +
		  ", sessionId=" + session['sessionId'])

	intent = intent_request['intent']
	intent_name = intent_request['intent']['name']

	if intent_name == "welcomeHello":
		return welcomeHello(intent, session)
	elif intent_name == "Contraceptives":
		return contraceptives(intent, session)
	elif intent_name == "Resources":
		return resources(intent, session)
	elif intent_name == "Health":
		return health(intent, session)
	elif intent_name == "AMAZON.CancelIntent":
		return end_session(session)
	elif intent_name == "AMAZON.StopIntent":
		return end_session(session)
	elif intent_name == "AMAZON.HelpIntent":
		return get_welcome_response()
	elif intent_name == "DomesticViolence":
		return domesticViolence(intent, session)
	else:
		raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
	""" Called when the user ends the session.
	Is not called when the skill returns should_end_session=true
	"""
	print("on_session_ended requestId=" + session_ended_request['requestId'] +
		", sessionId=" + session['sessionId'])

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
	session_attributes = {}
	card_title = "Welcome"
	speech_output = "You've started the Women's Access Health Skill. " \
					"How can I help you today?"
	# If the user either does not reply to the welcome message or says something
	# that is not understood, they will be prompted again with this text.
	reprompt_text = "I didn't catch that, what would you like help with?"
	should_end_session = False
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))


def end_session(session):
	should_end_session = True
	speech_output = "Ending your W A H session, hope I helped."
	reprompt_text = None
	session_attributes = {}
	card_title = "Stop"
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))

def welcomeHello(intent, session):
	try:
		session_attributes
	except NameError:
		session_attributes = {}

	should_end_session = False
	card_title = intent['name']

	speech_output = "How can I help you today?"
	reprompt_text = "I didn't quite catch that, could you say it again?"
	
	print("welcome Hello")
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))

def contraceptives(intent, session):
	try:
		session_attributes
	except NameError:
		session_attributes = {}

	reprompt_text = "I didn't quite catch that, could you say it again?"

	should_end_session = False
	card_title = intent['name']
	try:
		input = intent['slots']['ContraType']['value']
	except:
		input = False

	if input:
		if input == "abstinence":
			speech_output = "Abstinence is when you do not engage in any sort of sexual activity at any time. This is the only 100 percent effective way to ensure you do not become pregnant or contract a sexually transmitted disease"
		elif input == "the patch":
			speech_output = "A birth control patch is commonly known as Ortho Evra (or Evra patch). The beige patch sticks to the skin and helps prevent pregnancy. The patch is applied to the skin once a week for three weeks straight. The fourth week does not require a patch. When the patch is applied to the skin correctly, for the three week duration, it is over 99 percent effective at preventing pregnancy."
		elif input == "vaginal ring":
			speech_output = "A birth control vaginal ring is commonly known by the brand name NuvaRing. It is a small, flexible ring that a woman inserts into her vagina once a month to prevent pregnancy. It stays there for a three week period and is taken out for the last week of the month. When used correctly, the NuvaRing is over 99 percent effective at preventing pregnancy."
		elif input == "the pill":
			speech_output = "Birth control pills are a medication that women take on a daily basis to prevent pregnancy. Sometimes they are referred to as oral contraception or the pill. This birth control method is over 99 percent effective at preventing pregnancy, when taken correctly at the same time every day"
		elif input == "condoms":
			speech_output = "Both regular and female condoms are the only form of birth control that will help protect against S. T. Is and H.I.V. So even if you are using other birth control methods, it is important to use one to avoid infections. Since no birth control method is 100 percent effective, using a backup method like a condom just adds protection. Condoms reduce your risk of becoming pregnant"
		elif input == "female condoms":
			speech_output = "A female condom is a pouch that you put inside the vagina to reduce the risk of pregnancy. There are several brands of female condoms including Femidom, FC2, Reality and Protectiv. Most female condoms contain polyurethane, synthetic nitrile, or latex. They are composed of big and small rings located at open and closed ends of the condom. The small ring, at the closed end, is inserted into the vagina. The bigger ring, at the open end, remains outside of the vagina during intercourse. When used alone, female condoms are not the most effective birth control option. Among women who always use it correctly, 5 out of 100 will become pregnant. Among women who may not always use it correctly, 21 out of 100 will become pregnant. It is best to use female condoms in conjunction with another birth control method."
		elif input == "pull out" or input == "pulling out" or input == "the pull out method":
			speech_output = "Also known as the pull-out method, withdrawal involves removing the penis from the vagina before ejaculation occurs. This is done in order to prevent insemination from taking place. Considering withdrawal to be a legitimate form of birth control is the subject of some debate. However, it does function in lowering the likelihood of impregnation to some extent. Withdrawal will result in pregnancy in 4 out of 100 women who use this as their only form of birth control for one year. This is assuming perfect technique is employed."
		elif input == "spermicide":
			speech_output = "Spermicide is a substance which reduces the risk of pregnancy by heavily reducing sperm movement. It usually comes in the form of cream, gel, foam, film or suppositories. Spermicide is commonly used in conjunction with other birth control methods, but it can also reduce the risk of pregnancy on its own."
		elif input == "female sterilization" or input == "getting tubes tied":
			speech_output = "Tubal Ligation is also known as Tubal Sterilization or Sterilization for women. It is a permanent procedure that women undergo to prevent pregnancy. During this procedure, a health care professional will close or block a womans fallopian tubes. This birth control option is nearly 100 percent effective. Keep in mind that this birth control method does not protect against S. T. D. s. A male or female condom should be used to reduce risks of those infections"
		elif input == "vasectomies":
			speech_output = "Vasectomy is a form of birth control for men that is meant to be permanent. During vasectomy, a health care provider closes or blocks the tubes that carry sperm. When the tubes are closed, sperm cannot leave a man's body and cause pregnancy. It is safe and effective Costs \$0 to \$1,000 Meant to be permanent."
		elif input == "implants":
			speech_output = "The birth control implant (AKA Nexplanon) is a tiny, thin rod about the size of a matchstick. The implant releases hormones into your body that prevent you from getting pregnant. A nurse or doctor inserts the implant into your arm and that's it - you're protected from pregnancy for up to 4 years. Costs between \$0 and \$800 up front, but lasts up to 4 years"
		elif input == "i. u. dees.":
			speech_output = "An I.U.D. (Intrauterine Device) is a small t-shaped device that is made out of flexible plastic. The t-shaped device is inserted into a womans uterus to prevent pregnancy. It is an effective, long-term birth control method. However, if you ever do want to become pregnant, the I.U.D. can easily be removed because they are not permanent. An I.U.D. is one of the most effective methods of birth control. It is over 99 percent effective at preventing pregnancy."
		else:
			speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"


		return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))


	#input = intent['slots']['GeneralInput']['value']
	#speech = choose(input)
	speech_output = "A non-comprehensive list of contraceptive options includes: Abstinence, birth control patch, vaginal ring, birth control pills, condoms, female condoms, the pull out method, spermicide, female sterilization, vasectomies, implants,and I U Ds"
	
	
	print("Contraceptives")
	print(input)
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))


def plsMapQuest(requestType):
	requestSplit = requestType.split()
	resp = requests.get('https://searchahead-public-api-b2c-production.cloud.mapquest.com/search/v3/prediction?collection=address,adminArea,airport,category,franchise,poi&feedback=true&key=25nAMtQr6VVFyKqGtAZpF6KzU6O0Cb4G&limit=7&location= -105.270064,40.007325&q='+requestSplit[0]+'+'+requestSplit[1])
	resp = resp.json()

	checker0 = resp["results"]
	checker1 = checker0[0]
	checker2 = checker1["place"]
	checker = checker2["properties"]

	streetFull = checker['street']

	streetBits = streetFull.split(" ")
	print(streetBits[0])
	print(streetBits)
	zipcode = checker.get("postalCode")
	state = checker.get("stateCode")
	city = checker.get("city")
	#print("POOOOTTTTAAAATTTTTOOOO")
	newRequest = "https://www.mapquestapi.com/directions/v2/route?key=25nAMtQr6VVFyKqGtAZpF6KzU6O0Cb4G&from=80309&to="+streetBits[0]+'+'+streetBits[1]+'+'+streetBits[2]+'%2C'+city+'%2C'+state+zipcode+"&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"
	print(newRequest)
	resp2 = requests.get(newRequest)
	resp2 = resp2.json()
	#print(resp2)
	router = resp2.get('route')
	distance = router.get('distance')
	print(distance)
	resp3 = requests.get("https://www.mapquestapi.com/search/v2/radius?origin="+streetBits[0]+'+'+streetBits[1]+'+'+streetBits[2]+'%2C'+city+'%2C'+state+zipcode+"&radius=0.15&maxMatches=1&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|805999&outFormat=json&key=25nAMtQr6VVFyKqGtAZpF6KzU6O0Cb4G")
	resp3 = resp3.json()
	resultS = resp3.get("searchResults")
	pNu = resultS[0]["fields"]["phone"]
	print(pNu)
	temp = '-'
	temp = temp
	#"+(1)-(303)-4471040"
	pNu = str(pNu[6]+' '+pNu[7]+' '+pNu[8]+' '+pNu[11]+' '+pNu[12]+' '+pNu[13]+' '+pNu[14]+' '+pNu[15]+' '+pNu[16]+' '+pNu[17])
	#phoneNumReadable = '-'.join(phoneNum.join(e for e in string if e.isalnum()))
	speechOuter = "I've found a "+requestType+" in " + city + " " + str(distance) + " miles from you.  They are located at "+streetFull+" "+city+". Their phone number is " + pNu
	return speechOuter

def resources(intent, session):
	try:
		session_attributes
	except NameError:
		session_attributes = {}

	should_end_session = False
	card_title = intent['name']

	reprompt_text = "I didn't quite catch that, could you say it again?"

	try:
		input = intent['slots']['ResourceType']['value']
	except:
		input = False

	if input:
		if input == "planned parenthood":
			wannaSay = plsMapQuest("planned parenthood")
			speech_output = wannaSay
		elif input == "abuse clinic" or input == "abuse clinics":
			wannaSay = plsMapQuest("boulder domestic")
			speech_output = wannaSay
		elif input == "clinics" or input == "clinic" or input == "resource" or input == "resource center":
			wannaSay = plsMapQuest("womens clinic")
			speech_output = wannaSay
		elif input == "health clinics" or input == "health clinic" or input == "womens health":
			wannaSay = plsMapQuest("womens health")
			speech_output = wannaSay
		else:
			speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"


		return build_response(session_attributes, build_speechlet_response(
			card_title, speech_output, reprompt_text, should_end_session))

	speech_output = "I can help you find planned parenthood, womens resource centers, and abuse clinics"	
	
	print("Resources")
	print(input)
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))

def health(intent, session):
	try:
		session_attributes
	except NameError:
		session_attributes = {}

	reprompt_text = "I didn't quite catch that, could you say it again?"

	should_end_session = False
	card_title = intent['name']
	try:
		input = intent['slots']['HealthType']['value']
	except:
		input = False

	if input:
		if input == "what is consent":
			speech_output = "Consent is an agreement between participants to engage in sexual activity. There are many ways to give consent. Consent doesn't have to be verbal, but verbally agreeing to different sexual activities can help both you and your partner respect each others boundaries."
		elif input == "I missed my period" or input == "what happens if I miss my period":
			speech_output = "Don't freak out, there are more reasons than just being pregnant for a missed period. Have you been going through a lot of stress lately? That can cause a late or missed period. As well as extreme exercise, weight loss or weight gain, eating disorders, starting a new birth control, or it could be your body still working out your cycle. If you're concerned " + plsMapQuest("womens health")
		elif input == "what do I do if I think I have an s. t. d." or input == "I think I have an s. t. d.":
			speech_output = "It's much better to know whether or not you have an STD than to think you might have one. Therefore, the best thing to do when you are worried that you might have an STD is to find out whether or not you're right. You have to visit a doctor, a public agency, or a clinic to know for sure." + plsMapQuest("womens health")
		elif input == "how do I put on a condom":
			speech_output = "Check the expiration date, open the package carefully. don't use your fingernails - and don't use your teeth! and remove the condom from the wrapper. Hold the condom so it looks like a hat with the thick rolled-up part on the outside. As you look at it, you'll be able to see how you would roll it easily over an erect penis. Pinch the tip of the condom. Keep pinching the tip as you place the condom on the head of the erect penis and rolling it down all the way to the base of the penis"
		elif input == "what do I do about cramps":
			speech_output = "You can take a nonsteroidal anti-inflammatory medication like ibuprofen or naproxen. You can also improve your diet by adding vegetables and reducing fat to help manage period cramps."
		elif input == "i have a heavy period" or input == "my flow is heavy":
			speech_output = "If you're experiencing a heavy menstrual bleeding and it's getting in the way of your life, you should schedule an appointment with your primary care doctor or Obstetrics and Gynecology doctor."
		elif input == "What should I do if I am spotting":
			speech_output = "Spotting is any light vaginal bleeding which occurs at any time other than when a period is due. Spotting between periods is reasonably common. There can be a few reasons why it happens but the most common are hormonal changes and it being due to an implantation bleed."
		elif input == "How do you wash out period blood" or input == "How do you wash out blood":
			speech_output = "You can wash out blood stains using vinegar, ammonia, or hydrogen peroxide. Just remember to use preferably ice-cold water otherwise you might set the stain."
		elif input == "I've been sexually assaulted and need help" or input ==  "What do i do as a victim" or input == "I've been sexually assaulted":
			speech_output = "Recognising that there is a problem is the first stage of getting help. The best course of action is to talk to someone you can trust. " + plsMapQuest("boulder domestic")
		elif input == "My boyfriend hit me what do i do" or input == "My girlfriend hit me what do i do" or input == "My husband hit me what do i do" or input == "My wife hit me what do i do" or input == "My partner hit me what do i do":
			speech_output = "First you should make sure you're somewhere you feel safe. Then it's important to talk to someone who's there to help you about this." + plsMapQuest("boulder domestic")
		elif input == "What is Domestic Violence":
			speech_output = "Domestic Violence is violent or aggressive behavior within the home, typically involving the violent abuse of a spouse or partner"
		elif input == "What is the Law against Domestic Violence":
			speech_output = "In Colorado, domestic violence is defined as any crime committed as a means of coercion, control, punishment, intimidation, or revenge against an intimate partner, not only an act of violence. If officers are called out and they have probable cause to believe someone committed an act of Domestic Violence, the suspect of the crime must be arrested. Under the Colorado Constitution, some crimes are considered victims' rights cases. By definition, all Domestic Violence crimes are victim's rights cases. This means that the victim has several rights, including the right to consult with the DA before any offers are made and when bond is addressed. They have the right to speak at sentencing and to be notified when an incarcerated defendant will be released."
		else:
			speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"


		return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))


	#input = intent['slots']['GeneralInput']['value']
	#speech = choose(input)
	speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"
	
	
	print("Contraceptives")
	print(input)
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))

def domesticViolence(intent, session):
	try:
		session_attributes
	except NameError:
		session_attributes = {}

	reprompt_text = "I didn't quite catch that, could you say it again?"

	should_end_session = False
	card_title = intent['name']
	
	DomesticList=["1 in 3 women and 1 in 4 men have been victims of some form of physical violence by an intimate partner within their lifetime.", "On average, nearly 20 people per minute are physically abused by an intimate partner in the United States. During one year, this equates to more than 10 million women and men", "On a typical day, there are more than 20,000 phone calls placed to domestic violence hotlines nationwide.", "Intimate partner violence accounts for 15 percent of all violent crime.", "The cost of intimate partner violence exceeds $8.3 billion per year.", "Women abused by their intimate partners are more vulnerable to contracting H.I.V or other S.T.Is due to forced intercourse or prolonged exposure to stress.", "Studies suggest that there is a relationship between intimate partner violence and depression and suicidal behavior."]
	SexualList = ["1 in 5 women and 1 in 71 men in the United States has been raped in their lifetime.", "Almost half of female (46.7 percent) and male (44.9 percent) victims of rape in the United States were raped by an acquaintance. Of these, 45.4 percent of female rape victims and 29 percent of male rape victims were raped by an intimate partner.", "19.3 million women and 5.1 million men in the United States have been stalked in their lifetime. 60.8 percent of female stalking victims and 43.5 percent men reported being stalked by a current or former intimate partner.", "Women abused by their intimate partners are more vulnerable to contracting H.I.V or other S.T.Is due to forced intercourse or prolonged exposure to stress.", "Studies suggest that there is a relationship between intimate partner violence and depression and suicidal behavior."]
	
	try:
		input = intent['slots']['DomesticType']['value']
	except:
		input = False

	if input:
		if input == "domestic violence":
			speech_output = DomesticList[random.randrange(len(DomesticList))]
		elif input == "sexual violence": 
			speech_output = SexualList[random.randrange(len(SexualList))]
		else:
			speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"


		return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))


	#input = intent['slots']['GeneralInput']['value']
	#speech = choose(input)
	speech_output = "I'm sorry, I didn't understand that. Can you try a different request?"
	
	
	print("Contraceptives")
	print(input)
	return build_response(session_attributes, build_speechlet_response(
		card_title, speech_output, reprompt_text, should_end_session))

# --------------- Helpers that build all of the responses ----------------------
#????

def build_speechlet_response(title, output, reprompt_text, should_end_session):
	return {
		'outputSpeech': {
			'type': 'PlainText',
			'text': output
		},
		'card': {
			'type': 'Simple',
			'title': 'SessionSpeechlet - ' + title,
			'content': 'SessionSpeechlet - ' + output
		},
		'reprompt': {
			'outputSpeech': {
				'type': 'PlainText',
				'text': reprompt_text
			}
		},
		'shouldEndSession': should_end_session
	}


def build_response(session_attributes, speechlet_response):
	return {
		'version': '1.0',
		'sessionAttributes': session_attributes,
		'response': speechlet_response
	}