delete from eventscategories where true;
delete from eventsorganization where true;
delete from eventsuser where true;
delete from uni_faq where true;
delete from uni_events where true;
delete from uni_university where true;
delete from uni_categories where true;
delete from uni_postitions where true;
delete from uni_volunteer where true;
delete from uni_user where true;
delete from uni_organization where true;
delete from userpreferences where true;
delete from uni_features where true;
delete from uni_testimonials where true;



insert into uni_university
values (1, 'AUEB');

insert into uni_university
values (2, 'NTUA');


insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (1, 'PlanBiz', 'PlanBiz is an immersive business event that brings together industry leaders to explore innovative strategies and foster collaborative networking'
, 'Marousi, Athens', '2023-05-25 10:00:00', 100, 0 ,4.5,'../../images/planbiz.jpeg', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');


insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (2, 'ThinkBiz', 'ThinkBiz is an inspiring event that brings together visionary thinkers and entrepreneurs to explore innovative ideas and drive business growth'
, 'Aegaleo, Athens', '2023-05-15 10:00:00', 100, 0 , 4.9,'../../images/thinkbiz.png', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (3, 'TechConnect', 'TechConnect is a dynamic networking event that connects technology enthusiasts, professionals, and innovators to foster collaboration and drive technological advancements'
, 'Keramikos, Athens', '2023-05-02 10:00:00', 75, 0 , 4.9,'../../images/techconnect.jpeg', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (4, 'Open Conference', 'Open Conference, hosted by OpenAI, is a pioneering event that showcases groundbreaking advancements in artificial intelligence and promotes open collaboration and knowledge sharing'
, 'Megaro Mousikis, Athens', '2023-05-02 10:00:00', 500, 50 , 5,'../../images/openai.png', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (5, 'TedxAUEB Pangea Main Event', 'TEDxAUEB Pangea event brought together diverse speakers to share ideas on bridging global challenges through innovation and collaboration.'
, 'Viktoria, Athens', '2023-05-25 10:00:00', 200, 10 , 3.5,'../../images/pangea.webp', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (6, 'TedxNTUA Play Main Event', 'TEDxNTUA Play Main Event is an engaging platform where creative minds converge to explore the transformative power of play and its impact on innovation and personal growth'
, 'Zografou, Athens', '2023-05-15 10:00:00', 200, 10 , 4.5,'../../images/play.jpeg', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (7, 'FSDET Sustainability', 'FSDET Sustainability is a forward-thinking conference that addresses the pressing global challenges of sustainability, fostering discussions and solutions for a more environmentally conscious future.'
, 'Keramikos, Athens', '2023-05-30 10:00:00', 200, 10 , 4.5,'../../images/fsdet.png', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');


insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (8, 'Party at NTUA', 'Party at NTUA is an exciting and vibrant event where students and guests come together to celebrate, unwind, and create unforgettable memories'
, 'Zografou, Athens', '2023-05-30 23:00:00', 500, 10 , 5.0,'../../images/ntua_party.jpeg', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');



insert into uni_categories
values (1, 'StartUps', 'StartUps', 'Networking events that connect entrepreneurs with investors, mentors, and other like-minded individuals to discuss business ideas, strategies, and funding opportunities.
');

insert into uni_categories
values (2, 'Tech', 'Technology', 'Conferences and exhibitions that showcase the latest advancements in technology, including emerging fields such as artificial intelligence, blockchain, and virtual reality.
');

insert into uni_categories
values (3, 'TEDxEvents', 'TEDxEvents', 'Inspirational speeches by thought leaders from various fields, covering topics ranging from technology, science, and culture to global issues and personal growth.
');


insert into uni_categories
values (4, 'Uni', 'University', 'Educational events hosted by universities, featuring speakers, workshops, and networking opportunities for students, professionals, and academics, covering various fields of study and research.
');

insert into eventscategories
values (1, 1, 1);

insert into eventscategories
values (2, 1, 2);

insert into eventscategories
values (3, 2, 3);

insert into eventscategories
values (4, 2, 4);

insert into eventscategories
values (5, 3, 5);

insert into eventscategories
values (6, 3, 6);

insert into eventscategories
values (7, 4, 7);

insert into eventscategories
values (8, 4, 8);


--PlanBiz

insert into uni_postitions
values (1, 'Business Strategy Advisor', 'Provide strategic guidance and expertise to businesses attending PlanBiz event', '../../images/shield-icon.svg', 1);

insert into uni_postitions
values (2, 'Networking Facilitator', 'Assist in facilitating networking sessions and connecting industry leaders', '../../images/support-icon.svg', 1);

insert into uni_postitions
values (3, 'Event Coordinator', 'Help in coordinating logistics and ensuring a smooth flow of the PlanBiz event', '../../images/customize-icon.svg', 1);

insert into uni_postitions
values (4, 'Social Media Marketer', 'Promote PlanBiz event through social media channels and engage with online audience', '../../images/fast-icon.svg', 1);

insert into uni_postitions
values (5, 'Content Writer', 'Create engaging content, such as blog posts and articles, related to PlanBiz event', '../../images/reliable-icon.svg', 1);

insert into uni_postitions
values (6, 'Data Analyst', 'Analyze data collected during PlanBiz event and provide insights for future improvements', '../../images/simple-icon.svg', 1);


--ThinkBiz

insert into uni_postitions
values (7, 'Innovation Workshop Facilitator', 'Lead interactive workshops to foster innovative thinking and idea generation', '../../images/workshop-icon.svg', 2);

insert into uni_postitions
values (8, 'Startup Mentor', 'Provide guidance and mentorship to aspiring entrepreneurs attending ThinkBiz event', '../../images/mentor-icon.svg', 2);

insert into uni_postitions
values (9, 'Marketing Strategist', 'Develop marketing strategies and campaigns to promote ThinkBiz event', '../../images/marketing-icon.svg', 2);

insert into uni_postitions
values (10, 'Speaker Liaison', 'Coordinate with speakers and ensure smooth communication before and during ThinkBiz event', '../../images/liaison-icon.svg', 2);

insert into uni_postitions
values (11, 'Event Photographer', 'Capture memorable moments and document the ThinkBiz event through photography', '../../images/photography-icon.svg', 2);

insert into uni_postitions
values (12, 'Graphic Designer', 'Design visually appealing promotional materials and graphics for ThinkBiz event', '../../images/designer-icon.svg', 2);

--TechConnect

insert into uni_postitions
values (13, 'Tech Demo Presenter', 'Demonstrate innovative technologies and products at the TechConnect event', '../../images/simple-icon.svg', 3);

insert into uni_postitions
values (14, 'Panel Discussion Moderator', 'Moderate panel discussions and facilitate engaging conversations at TechConnect event', '../../images/fast-icon.svg', 3);

insert into uni_postitions
values (15, 'Tech Blogger', 'Write insightful blog posts and articles covering the latest technology trends discussed at TechConnect event', '../../images/reliable-icon.svg', 3);

insert into uni_postitions
values (16, 'Audiovisual Technician', 'Provide technical support for audiovisual setup and equipment during TechConnect event', '../../images/customize-icon.svg', 3);

insert into uni_postitions
values (17, 'Startup Pitch Judge', 'Evaluate and provide feedback on startup pitches during the TechConnect event', '../../images/support-icon.svg', 3);

insert into uni_postitions
values (18, 'Virtual Reality Experience Coordinator', 'Assist attendees in exploring virtual reality experiences showcased at TechConnect event', '../../images/shield-icon.svg', 3);



--Open Conference

insert into uni_postitions
values (19, 'AI Research Presenter', 'Present groundbreaking AI research and advancements at the Open Conference', '../../images/support-icon.svg', 4);

insert into uni_postitions
values (20, 'Workshop Facilitator', 'Lead interactive workshops on AI-related topics during the Open Conference', '../../images/shield-icon.svg', 4);

insert into uni_postitions
values (21, 'Event Volunteer Coordinator', 'Coordinate and manage volunteers to ensure smooth operations at the Open Conference', '../../images/customize-icon.svg', 4);

insert into uni_postitions
values (22, 'Social Media Coordinator', 'Manage social media presence and engagement for the Open Conference', '../../images/reliable-icon.svg', 4);

insert into uni_postitions
values (23, 'Documentation Specialist', 'Document key insights and takeaways from the sessions and presentations at the Open Conference', '../../images/simple-icon.svg', 4);

insert into uni_postitions
values (24, 'Event Photographer', 'Capture moments and document the Open Conference through photography', '../../images/fast-icon.svg', 4);



-- TedxPangea

insert into uni_postitions
values (25, 'Ads Management', 'We create and manage ads that you need, from creation to deployment', '../../images/shield-icon.svg', 5);

insert into uni_postitions
values (26, 'Video Marketing', 'Video marketing involves creating and sharing videos to promote a brand, product, or service to a target audience.', '../../images/support-icon.svg', 5);

insert into uni_postitions
values (27, 'Customer Relation', 'Customer relation is the process of building and maintaining positive relationships with customers to enhance loyalty and satisfaction.', '../../images/customize-icon.svg', 5);

insert into uni_postitions
values (28, 'Product Outreach', 'Product outreach refers to the process of promoting a product to a new or existing target audience to increase awareness and sales.', '../../images/reliable-icon.svg', 5);

insert into uni_postitions
values (29, 'PR Campaign', 'A PR campaign is a planned effort to create and maintain a positive public image and reputation for a company or individual through media coverage.', '../../images/fast-icon.svg', 5);

insert into uni_postitions
values (30, 'Product Expansion', 'Product expansion is the process of developing and introducing new products or features to an existing product line to increase revenue and market share.', '../../images/simple-icon.svg', 5);


--TedxNTUA Play

insert into uni_postitions
values (31, 'Play Workshop Facilitator', 'Lead interactive workshops and activities focused on the theme of play during TedxNTUA Play Main Event', '../../images/fast-icon.svg', 6);

insert into uni_postitions
values (32, 'Speaker Liaison', 'Coordinate with speakers and ensure smooth communication before and during TedxNTUA Play Main Event', '../../images/reliable-icon.svg', 6);

insert into uni_postitions
values (33, 'Event Photographer', 'Capture memorable moments and document the TedxNTUA Play Main Event through photography', '../../images/customize-icon.svg', 6);

insert into uni_postitions
values (34, 'Social Media Coordinator', 'Promote TedxNTUA Play event on various social media platforms and engage with the online audience', '../../images/support-icon.svg', 6);

insert into uni_postitions
values (35, 'Stage Designer', 'Design the stage setup and decorations for TedxNTUA Play Main Event', '../../images/shield-icon.svg', 6);

insert into uni_postitions
values (36, 'Graphic Designer', 'Create visually appealing promotional materials and graphics for TedxNTUA Play event', '../../images/simple-icon.svg', 6);



--FSDET

insert into uni_postitions
values (37, 'Workshop Facilitator', 'Lead interactive workshops on sustainability and environmental conservation during FSDET Sustainability event', '../../images/customize-icon.svg', 7);

insert into uni_postitions
values (38, 'Panel Discussion Moderator', 'Moderate panel discussions and facilitate engaging conversations on sustainability topics at FSDET Sustainability event', '../../images/support-icon.svg', 7);

insert into uni_postitions
values (39, 'Event Photographer', 'Capture moments and document the FSDET Sustainability event through photography', '../../images/shield-icon.svg', 7);

insert into uni_postitions
values (40, 'Social Media Coordinator', 'Manage social media presence and engagement for the FSDET Sustainability event', '../../images/simple-icon.svg', 7);

insert into uni_postitions
values (41, 'Volunteer Coordinator', 'Coordinate and manage volunteers to ensure smooth operations at the FSDET Sustainability event', '../../images/fast-icon.svg', 7);

insert into uni_postitions
values (42, 'Sustainability Advocate', 'Promote sustainable practices and raise awareness about environmental issues during FSDET Sustainability event', '../../images/reliable-icon.svg', 7);



--Party

insert into uni_postitions
values (44, 'Event DJ', 'Create a lively and energetic atmosphere by DJing at the Party at NTUA', '../../images/shield-icon.svg', 8);

insert into uni_postitions
values (45, 'Bartender', 'Prepare and serve drinks at the bar during the Party at NTUA', '../../images/customize-icon.svg', 8);

insert into uni_postitions
values (46, 'Event Photographer', 'Capture fun and memorable moments of the Party at NTUA through photography', '../../images/fast-icon.svg', 8);

insert into uni_postitions
values (47, 'Decorations Team', 'Assist in setting up and decorating the venue for the Party at NTUA', '../../images/support-icon.svg', 8);

insert into uni_postitions
values (48, 'Promotions Team', 'Promote the Party at NTUA event and distribute flyers and promotional materials', '../../images/reliable-icon.svg', 8);

insert into uni_postitions
values (49, 'Security Staff', 'Ensure the safety and security of attendees during the Party at NTUA', '../../images/simple-icon.svg', 8);

-- Pos 50, Event Organizer for Event 1 PlanBiz
insert into uni_postitions
values (50, 'Event Organizer', 'An event coordinator for event plans, organizes, and manages the logistics, speakers, and overall experience of the event', '-', 1);

-- Pos 51 Website, Coordinator for Event 1 PlanBiz
insert into uni_postitions
values (51, 'Website, Coordinator', 'The website coordinator is responsible for managing and maintaining the website of an organization or event, ensuring its functionality, user experience, and up-to-date information.', '-', 1);

-- Pos 52 Jr. Designer for Event 2 ThinkBiz
insert into uni_postitions
values (52, 'Jr. Designer', 'Assisting in creating visually appealing designs, collaborating with the team, and contributing to creative projects', '-', 2);

-- Pos 53 Lead Developer for Event 2 ThinkBiz
insert into uni_postitions
values (53, 'Lead Developer', 'Responsible for leading a team of developers, overseeing project development, and ensuring high-quality code and technical solutions.', '-', 2);

--Pos 54 Sr. Developer for Event 3 TechConnect
insert into uni_postitions
values (54, 'Sr. Developer', 'Experienced developer specializing in complex systems, providing technical expertise, and driving software development projects to success.', '-', 3);

--Pos 55 Quality Assurance for Event 3 TechConnect
insert into uni_postitions
values (55, 'Quality Assurance', 'Ensuring software quality by implementing testing processes, identifying and reporting bugs, and maintaining product standards and reliability', '-', 3);

--Pos 56 Marketing Specialist for Event 4 OpenAI
insert into uni_postitions
values (56, 'Marketing Specialist', 'Developing and executing marketing strategies, conducting market research, and driving brand awareness and customer engagement.', '-', 4);

--Pos 57 Content Writer for Event 4 OpenAI
insert into uni_postitions
values (57, 'Content Writer', 'Creating engaging and informative content for various platforms, including websites, blogs, social media, and marketing materials.', '-', 4);

--Pos 58 Sales Representative for Event 5 pangea
insert into uni_postitions
values (58, 'Sales Representative', 'Identifying and acquiring new customers, maintaining client relationships, and achieving sales targets through effective communication and negotiation.', '-', 5);

--Pos 59 Data Analyst for Event 5 pangea
insert into uni_postitions
values (59, 'Data Analyst', 'Collecting, analyzing, and interpreting data to provide insights and support data-driven decision-making for business operations and strategies.', '-', 5);

--Pos 60 Social Media Manager for Event 6 play
insert into uni_postitions
values (60, 'Social Media Manager', 'Managing and executing social media strategies, creating engaging content, and monitoring online presence and audience engagement.', '-', 6);

--Pos 61 Project Coordinator for Event 6 play
insert into uni_postitions
values (61, 'Project Coordinator', 'Coordinating project activities, monitoring progress, ensuring timely delivery, and facilitating communication among team members and stakeholders.', '-', 6);

--Pos 62 Research Analyst for Event 7 fsdet
insert into uni_postitions
values (62, 'Research Analyst', 'Conducting market research, analyzing data, and generating insights to support strategic decision-making and business growth.', '-', 7);

--Pos 63 Event Planner for Event 7 fsdet
insert into uni_postitions
values (63, 'Event Planner', 'Planning and organizing events, managing budgets, coordinating logistics, and ensuring a seamless and memorable event experience.', '-', 7);

--Pos 64 Customer Support Specialist for Event 8 party
insert into uni_postitions
values (64, 'Customer Support Specialist', 'Providing timely and helpful assistance to customers, resolving inquiries and issues, and ensuring high levels of customer satisfaction.', '-', 8);

--Pos 65 Financial Analyst for Event 8 party
insert into uni_postitions
values (65, 'Financial Analyst', 'Analyzing financial data, preparing reports, forecasting financial performance, and providing recommendations to support financial decision-making.', '-', 8);



insert into uni_user
values (1, 'Charlotte', 'Hale', '08-01-2002', 'F', '-', 'ch@example.com', '-', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3.25&w=512&h=512&q=80', 'Keramikos, Athens', null);

insert into uni_user
values (2, 'Adam', 'Cuppy', '08-01-2002', 'M', '-', 'ac@example.com', '-', 'https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=512&h=512&q=80', 'Megaro Mousikis, Athens', null);

insert into uni_user
values (3, 'Silvester', 'Wize', '08-01-2002', 'M', '-', 'aw@example.com', '-', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3.25&w=512&h=512&q=80', 'Zografou, Athens', null);

insert into uni_user
values (4, 'Himali', 'Turn', '08-01-2002', 'F', '-', 'ht@example.com', '-', 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&fit=facearea&facepad=2.95&w=512&h=512&q=80', 'Aegaleo, Athens', null);

insert into uni_user
values (5, 'Troye', 'Turn', '08-01-2002', 'M', '-', 'tt@example.com', '-', 'https://images.unsplash.com/photo-1546820389-44d77e1f3b31?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&fit=facearea&facepad=3.45&w=512&h=512&q=80', 'Aegaleo, Athens', null);

insert into uni_user
values (6, 'Holo', 'Wo', '08-01-2002', 'F', '-', 'hw@example.com', '-', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&fit=facearea&facepad=3.45&w=512&h=512&q=80', 'Zografou, Athens', null);


--User 1 Vol 1 Pos 50, Event Organizer for Event 1 PlanBiz
insert into uni_volunteer
values (1, 50, 'I like to be a part in charge of a team, organize, and help develop something new.', 1, 'S');

insert into uni_testimonials
values (1, 'Planning at PlanBiz', 'Serving as Event Organizer for PlanBiz was truly rewarding. Seeing industry leaders come together to discuss innovative strategies due to my planning and management was a powerful experience.', 1);


--User 2 Vol 2 Pos 51 Website, Coordinator for Event 1 PlanBiz
insert into uni_volunteer
values (2, 51, 'As a Web Developer, I think I would be a great addition to the team.', 2, 'S');

insert into uni_testimonials
values (2, 'Website Management for PlanBiz', 'As a Website Coordinator for PlanBiz, I enjoyed ensuring that the website reflected the innovative ideas and growth-oriented discussions that took place during the event.', 2);


--User 3 Vol 3 Pos 52 Jr. Designer for Event 2 ThinkBiz
insert into uni_volunteer
values (3, 52, 'I am enthusiastic about volunteering and contributing to the success of events.', 3, 'S');

insert into uni_testimonials
values (3, 'Designing for ThinkBiz', 'Working as a Jr. Designer for ThinkBiz, I had the opportunity to create visually appealing designs for an event that brings together technology enthusiasts and innovators.', 3);


-- User 2 Vol 4 Pos 53 Lead Developer for Event 2 ThinkBiz
insert into uni_volunteer
values (4, 53, 'I have a passion for web development and would love to support the team with my skills.', 4, 'S');

insert into uni_testimonials
values (4, 'Leading Development at ThinkBiz', 'As Lead Developer for ThinkBiz, it was incredible to oversee project development in the cutting-edge field of artificial intelligence, making sure high-quality technical solutions were delivered.', 4);


-- User 5 Vol 6 Pos 54 Sr. Developer for Event 3 TechConnect
insert into uni_volunteer
values (5, 54, 'I enjoy taking on responsibilities, working in a team, and contributing to innovative projects.', 5, 'S');

insert into uni_testimonials
values (5, 'Developing for TechConnect', 'Being a Sr. Developer at TechConnect, I contributed my expertise in developing complex systems that supported an event focused on bridging global challenges through innovation and collaboration.', 5);


-- User 6 Vol 6 Pos 55 Quality Assurance for Event 3 TechConnect
insert into uni_volunteer
values (6, 55, 'With my expertise in web development, I can add value to the team and create impactful solutions.', 6, 'S');

insert into uni_testimonials
values (6, 'Ensuring Quality at TechConnect', 'As Quality Assurance for TechConnect, I was proud to help maintain the high standard of the event by implementing rigorous testing processes and maintaining product reliability.', 6);


-- User 1 Vol 7 Pos 56 Marketing Specialist for Event 4 OpenAI
insert into uni_volunteer
values (7, 56, 'I am eager to contribute to the success of events and assist with marketing initiatives.', 1, 'S');

insert into uni_testimonials
values (7, 'Marketing the OpenAI', 'As a Marketing Specialist for OpenAI, it was rewarding to develop strategies and conduct market research for a forward-thinking conference aimed at addressing global sustainability challenges.', 7);


-- User 2 Vol 8 Pos 57 Content Writer for Event 4 OpenAI
insert into uni_volunteer
values (8, 57, 'As a creative content writer, I can contribute engaging content to support the organization.', 2, 'S');

insert into uni_testimonials
values (8, 'Content Creation for OpenAI', 'As a Content Writer for OpenAI, I had the pleasure of creating engaging content for an event filled with excitement, celebration, and unforgettable memories.', 8);


-- User 3 Vol 9 Pos 58 Sales Representative for Event 5 pangea
insert into uni_volunteer
values (9, 58, 'I am motivated to connect with customers, drive sales, and achieve targets.', 3, 'S');

insert into uni_testimonials
values (9, 'Sales at TedxAUEB Pangea', 'As a Sales Representative at TedxAUEB Pangea, the chance to identify and acquire new customers in such a dynamic networking event was an experience that honed my communication and negotiation skills.', 9);


-- User 4 Vol 10 Pos 59 Data Analyst for Event 5 pangea
insert into uni_volunteer
values (10, 59, 'With my analytical skills, I can help uncover insights and support data-driven decision-making.', 4, 'S');

insert into uni_testimonials
values (10, 'Data Analysis for TedxAUEB Pangea', 'Being a Data Analyst at TedxAUEB Pangea, I was able to support the events innovative and growth-oriented approach by providing data-driven insights that informed business operations and strategies.', 10);


-- User 5 Vol 11 Pos 60 Social Media Manager for Event 6 play
insert into uni_volunteer
values (11, 60, 'I am experienced in managing social media and can contribute to engaging online presence.', 5, 'S');

insert into uni_testimonials
values (11, 'Social Media for TEDxNTUA Play', 'As a Social Media Manager for TEDxNTUA Play, I had the opportunity to create and manage engaging content that effectively promoted the groundbreaking advancements in artificial intelligence showcased at the event.', 11);


-- User 6 Vol 12 Pos 61 Project Coordinator for Event 6 play
insert into uni_volunteer
values (12, 61, 'As a project coordinator, I can ensure efficient communication and coordination within the team.', 6, 'S');

insert into uni_testimonials
values (12, 'Coordinating at TEDxNTUA Play', 'As a Project Coordinator at TEDxNTUA Play event, coordinating project activities and ensuring timely delivery was challenging yet rewarding, as it helped bridge global challenges through innovation and collaboration.', 12);


-- User 1 Vol 13 Pos 62 Research Analyst for Event 7 fsdet
insert into uni_volunteer
values (13, 62, 'I am passionate about research and can contribute valuable insights to support strategic decisions.', 1, 'S');

insert into uni_testimonials
values (13, 'Researching for FSDET Sustainability', 'As a Research Analyst for FSDET Sustainability, conducting market research and analyzing data to support strategic decision-making was rewarding. It was a pleasure to contribute to discussions and solutions for a more environmentally conscious future.', 13);


-- User 2 Vol 14 Pos 63 Event Planner for Event 7 fsdet
insert into uni_volunteer
values (14, 63, 'I have experience in event planning and can help create memorable and successful events.', 2, 'S');

insert into uni_testimonials
values (14, 'Planning Entertainment for FSDET Sustainability', 'Being an Entertainment Planner for FSDET Sustainability, it was fulfilling to create an exciting atmosphere where students and guests could unwind and create unforgettable memories.', 14);


-- User 3 Vol 15 Pos 64 Customer Support Specialist for Event 8 party
insert into uni_volunteer
values (15, 64, 'I am dedicated to providing excellent customer support and ensuring customer satisfaction.', 3, 'S');

insert into uni_testimonials
values (15, 'Customer Support Specialist NTUA Parties', 'Its always a great experience to host your event, even more so when you meet amazing people from your uni you had no idea existed', 15);


-- User 4 Vol 16 Pos 65 Financial Analyst for Event 8 party
insert into uni_volunteer
values (16, 65, 'With my financial analysis skills, I can provide valuable insights for informed decision-making.', 4, 'S');

insert into uni_testimonials
values (16, 'Financial Analyst for the NTUA Parties', 'Mostly in charge of register,  but let me tell you you got to keep a clear head to do the math, which is not easy considering all the fun of being at a party.', 16);




insert into uni_organization
values (1, 'ThinkBiz Academy', '-');

insert into uni_organization
values (2, 'Tech Conference Inc', '-');

insert into uni_organization
values (3, 'OpenAI', '-');

insert into uni_organization
values (4, 'TedxAUEB', '-');

insert into uni_organization
values (5, 'TedxNTUA', '-');

insert into uni_organization
values (6, 'DMST', '-');

insert into uni_organization
values (7, 'NTUA', '-');

insert into eventsorganization
values (1, 1, 1);

insert into eventsorganization
values (2, 2, 1);

insert into eventsorganization
values (3, 3, 2);

insert into eventsorganization
values (4, 4, 3);

insert into eventsorganization
values (5, 5, 4);

insert into eventsorganization
values (6, 6, 5);

insert into eventsorganization
values (7, 7, 6);

insert into eventsorganization
values (8, 8, 7);

insert into eventsuser
values (1, 5, 1, 5);

insert into eventsuser
values (2, 5, 2, 5);

insert into userpreferences
values (1, 1, 1);

insert into userpreferences
values (2, 2, 1);

insert into userpreferences
values (3, 3, 2);

insert into userpreferences
values (4, 4, 2);


-- Event 1 - PlanBiz
insert into uni_features
values (1, 'Speakers', '250+', 1);

insert into uni_features
values (2, 'Attendees', '1000+', 1);

insert into uni_features
values (3, 'Workshops', '50+', 1);

-- Event 2 - ThinkBiz
insert into uni_features
values (4, 'Elite Speakers', '15+', 2);

insert into uni_features
values (5, 'Engaged Attendees', '500+', 2);

insert into uni_features
values (6, 'Interactive Workshops', '10+', 2);


-- Event 3 - TechConnect
insert into uni_features
values (7, 'Expert Speakers', '20+', 3);

insert into uni_features
values (8, 'Enthusiastic Attendees', '300+', 3);

insert into uni_features
values (9, 'Informative Workshops', '8+', 3);


-- Event 4 - Open Conference
insert into uni_features
values (10, 'Keynote Speakers', '40+', 4);

insert into uni_features
values (11, 'Participants', '1000+', 4);

insert into uni_features
values (12, 'Breakout Sessions', '20+', 4);


-- Event 5 - TedxAUEB Pangea Main Event
insert into uni_features
values (13, 'Diverse Speakers', '12+', 5);

insert into uni_features
values (14, 'Global Attendees', '150+', 5);

insert into uni_features
values (15, 'Inspiring Workshops', '5+', 5);


-- Event 6 - TedxNTUA Play Main Event
insert into uni_features
values (16, 'Creative Speakers', '8+', 6);

insert into uni_features
values (17, 'Energetic Attendees', '100+', 6);

insert into uni_features
values (18, 'Innovative Workshops', '3+', 6);


-- Event 7 - FSDET Sustainability
insert into uni_features
values (19, 'Keynote Speakers', '10+', 7);

insert into uni_features
values (20, 'Green Companies', '200+', 7);

insert into uni_features
values (21, 'Action-oriented Workshops', '6+', 7);


-- Event 8 - Party at NTUA
insert into uni_features
values (22, 'Performances', '10+', 8);

insert into uni_features
values (23, 'Attendees', '1000+', 8);

insert into uni_features
values (24, 'DJs', '5+', 8);

-- Event 1 - PlanBiz
insert into uni_faq
values (1, 'What is the focus of the PlanBiz event?',
        'PlanBiz is an immersive business event that brings together industry leaders to explore innovative strategies and foster collaborative networking.', 1);

insert into uni_faq
values (2, 'Where is the PlanBiz event located?',
        'The PlanBiz event is located in Marousi, Athens.', 1);

insert into uni_faq
values (3, 'What is the capacity of the PlanBiz event?',
        'The capacity of the PlanBiz event is 100 attendees.', 1);


-- Event 2 - ThinkBiz
insert into uni_faq
values (4, 'What is the theme of the ThinkBiz event?',
        'ThinkBiz is an inspiring event that brings together visionary thinkers and entrepreneurs to explore innovative ideas and drive business growth.', 2);

insert into uni_faq
values (5, 'Where is the ThinkBiz event located?',
        'The ThinkBiz event is located in Aegaleo, Athens.', 2);

insert into uni_faq
values (6, 'What is the capacity of the ThinkBiz event?',
        'The capacity of the ThinkBiz event is 100 attendees.', 2);


-- Event 3 - TechConnect
insert into uni_faq
values (7, 'What is the focus of the TechConnect event?',
        'TechConnect is a dynamic networking event that connects technology enthusiasts, professionals, and innovators to foster collaboration and drive technological advancements.', 3);

insert into uni_faq
values (8, 'Where is the TechConnect event located?',
        'The TechConnect event is located in Keramikos, Athens.', 3);

insert into uni_faq
values (9, 'What is the capacity of the TechConnect event?',
        'The capacity of the TechConnect event is 75 attendees.', 3);


-- Event 4 - Open Conference
insert into uni_faq
values (10, 'What is the focus of the Open Conference event?',
        'Open Conference, hosted by OpenAI, is a pioneering event that showcases groundbreaking advancements in artificial intelligence and promotes open collaboration and knowledge sharing.', 4);

insert into uni_faq
values (11, 'Where is the Open Conference event located?',
        'The Open Conference event is located in Megaro Mousikis, Athens.', 4);

insert into uni_faq
values (12, 'What is the capacity of the Open Conference event?',
        'The capacity of the Open Conference event is 500 attendees.', 4);


-- Event 5 - TedxAUEB Pangea Main Event
insert into uni_faq
values (13, 'What is the theme of the TedxAUEB Pangea Main Event?',
        'The theme of the TedxAUEB Pangea Main Event is "Bridging Global Challenges through Innovation and Collaboration."', 5);

insert into uni_faq
values (14, 'Where is the TedxAUEB Pangea Main Event located?',
        'The TedxAUEB Pangea Main Event is located in Viktoria, Athens.', 5);

insert into uni_faq
values (15, 'What is the capacity of the TedxAUEB Pangea Main Event?',
        'The capacity of the TedxAUEB Pangea Main Event is 200 attendees.', 5);


-- Event 6 - TedxNTUA Play Main Event
insert into uni_faq
values (16, 'What is the theme of the TedxNTUA Play Main Event?',
        'The theme of the TedxNTUA Play Main Event is "Exploring the Transformative Power of Play."', 6);

insert into uni_faq
values (17, 'Where is the TedxNTUA Play Main Event located?',
        'The TedxNTUA Play Main Event is located in Zografou, Athens.', 6);

insert into uni_faq
values (18, 'What is the capacity of the TedxNTUA Play Main Event?',
        'The capacity of the TedxNTUA Play Main Event is 200 attendees.', 6);


-- Event 7 - FSDET Sustainability
insert into uni_faq
values (19, 'What is the focus of the FSDET Sustainability event?',
        'FSDET Sustainability is a forward-thinking conference that addresses the pressing global challenges of sustainability, fostering discussions and solutions for a more environmentally conscious future.', 7);

insert into uni_faq
values (20, 'Where is the FSDET Sustainability event located?',
        'The FSDET Sustainability event is located in Keramikos, Athens.', 7);

insert into uni_faq
values (21, 'What is the capacity of the FSDET Sustainability event?',
        'The capacity of the FSDET Sustainability event is 200 attendees.', 7);


-- Event 8 - Party at NTUA
insert into uni_faq
values (22, 'What is the focus of the Party at NTUA event?',
        'Party at NTUA is an exciting and vibrant event where students and guests come together to celebrate, unwind, and create unforgettable memories.', 8);

insert into uni_faq
values (23, 'Where is the Party at NTUA event located?',
        'The Party at NTUA event is located in Zografou, Athens.', 8);

insert into uni_faq
values (24, 'What is the capacity of the Party at NTUA event?',
        'The capacity of the Party at NTUA event is 500 attendees.', 8);





