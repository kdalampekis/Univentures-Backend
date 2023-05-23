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


insert into uni_postitions
values (1, 'Ads Management', 'We create and manage ads that you need, from creation to deployment', '../../images/shield-icon.svg', 5);

insert into uni_postitions
values (2, 'Video Marketing', 'Video marketing involves creating and sharing videos to promote a brand, product, or service to a target audience.', '../../images/support-icon.svg', 5);

insert into uni_postitions
values (3, 'Customer Relation', 'Customer relation is the process of building and maintaining positive relationships with customers to enhance loyalty and satisfaction.', '../../images/customize-icon.svg', 5);

insert into uni_postitions
values (4, 'Product Outreach', 'Product outreach refers to the process of promoting a product to a new or existing target audience to increase awareness and sales.', '../../images/reliable-icon.svg', 5);

insert into uni_postitions
values (5, 'PR Campaign', 'A PR campaign is a planned effort to create and maintain a positive public image and reputation for a company or individual through media coverage.', '../../images/fast-icon.svg', 5);

insert into uni_postitions
values (6, 'Product Expansion', 'Product expansion is the process of developing and introducing new products or features to an existing product line to increase revenue and market share.', '../../images/simple-icon.svg', 5);

insert into uni_postitions
values (7, 'Event Orginizer', 'An event coordinator for event plans, organizes, and manages the logistics, speakers, and overall experience of the event', '-', 5);

insert into uni_postitions
values (8, 'Website, Coordinator', 'The website coordinator is responsible for managing and maintaining the website of an organization or event, ensuring its functionality, user experience, and up-to-date information.', '-', 5);


insert into uni_faq
values (1, 'What is the theme of the TEDxAUEB event (Pangea)?',
        'The theme of the TEDxAUEB event is Pangea: Reconnecting Our World. ' ||
        'The event aims to explore ideas and initiatives that promote unity and interconnectedness in todays globalized world.', 5);

insert into uni_faq
values (2, 'What are some important things to consider when attending a TEDx event like TEDxAUEB Pangea ?',
        'Be prepared to listen: TEDx talks are all about ideas worth spreading, so be prepared to listen and engage with the speakers and their ideas.', 5);

insert into uni_faq
values (3, 'Who can attend the TEDxAUEB event Pangea?',
        'Anyone who is interested in TEDx talks and the theme of the event can attend the TEDxAUEB event (Pangea). However, attendees are required to purchase a ticket in advance to secure their spot.', 5);

insert into uni_faq
values (4, 'Who are the speakers at the TEDxAUEB event Pangea?',
        'The speakers at the TEDxAUEB event Pangea are experts and innovators from various fields, including technology, science, business, and the arts. ' ||
        'Their talks will revolve around the theme of the event, exploring ways to reconnect our world and build a better future for all.', 5);

insert into uni_user
values (1, 'Charlotte', 'Hale', '08-01-2002', 'F', '-', 'ch@example.com', '-', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3.25&w=512&h=512&q=80');

insert into uni_user
values (2, 'Adam', 'Cuppy', '08-01-2002', 'M', '-', 'ac@example.com', '-', 'https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=512&h=512&q=80');



insert into uni_volunteer
values (1, 'Amazing Attendee Experience', 'TEDxAUEB offers an exceptional experience with diverse speakers sharing inspiring ideas worth spreading. Attendees can connect with like-minded individuals, participate in interactive workshops, and explore new ideas. With high production value and attention to detail, TEDxAUEB ensures a seamless and memorable experience.
', 1, 7);


insert into uni_volunteer
values (2, 'Talk with amazing companies that helped organize the event', 'Speaking with the amazing companies that helped organize the TEDxAUEB event can offer insights into their roles and contributions. It allows for understanding of how their expertise, resources, and innovation helped bring the event to life, and how they aligned with the event''s values and vision.
', 2, 8);

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
values (1, 5, 1);

insert into eventsuser
values (2, 5, 2);


