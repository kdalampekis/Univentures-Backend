insert into uni_university
values (1, 'AUEB');

insert into uni_university
values (2, 'NTUA');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (1, 'PlanBiz', 'PlanBiz is an immersive business event that brings together industry leaders to explore innovative strategies and foster collaborative networking'
, 'Marousi, Athens', '25-05-2023 10:00:00', 100, 0 ,4.5,'../../images/planbiz.jpeg', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');


insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (2, 'ThinkBiz', 'ThinkBiz is an inspiring event that brings together visionary thinkers and entrepreneurs to explore innovative ideas and drive business growth'
, 'Aegaleo, Athens', '15-05-2023 10:00:00', 100, 0 , 4.9,'../../images/thinkbiz.png', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (3, 'TechConnect', 'TechConnect is a dynamic networking event that connects technology enthusiasts, professionals, and innovators to foster collaboration and drive technological advancements'
, 'Keramikos, Athens', '2-05-2023 10:00:00', 75, 0 , 4.9,'../../images/techconnect.jpeg', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (4, 'Open Conference', 'Open Conference, hosted by OpenAI, is a pioneering event that showcases groundbreaking advancements in artificial intelligence and promotes open collaboration and knowledge sharing'
, 'Megaro Mousikis, Athens', '2-05-2023 10:00:00', 500, 50 , 5,'../../images/openai.png', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (5, 'TedxAUEB Pangea Main Event', 'TEDxAUEB Pangea event brought together diverse speakers to share ideas on bridging global challenges through innovation and collaboration.'
, 'Viktoria, Athens', '25-05-2023 10:00:00', 200, 10 , 3.5,'../../images/pangea.webp', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (6, 'TedxNTUA Play Main Event', 'TEDxNTUA Play Main Event is an engaging platform where creative minds converge to explore the transformative power of play and its impact on innovation and personal growth'
, 'Zografou, Athens', '15-05-2023 10:00:00', 200, 10 , 4.5,'../../images/play.jpeg', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');

insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (7, 'FSDET Sustainability', 'FSDET Sustainability is a forward-thinking conference that addresses the pressing global challenges of sustainability, fostering discussions and solutions for a more environmentally conscious future.'
, 'Keramikos, Athens', '30-05-2023 10:00:00', 200, 10 , 4.5,'../../images/fsdet.png', 1, 'https://www.youtube.com/embed/KtRHV9gH83U');


insert into uni_events(id, title, description, location, timestamp, capacity, price, rating, img_src, university_id, video_src)
values (8, 'Party at NTUA', 'Party at NTUA is an exciting and vibrant event where students and guests come together to celebrate, unwind, and create unforgettable memories'
, 'Zografou, Athens', '30-05-2023 23:00:00', 500, 10 , 5.0,'../../images/ntua_party.jpeg', 2, 'https://www.youtube.com/embed/KtRHV9gH83U');



insert into uni_categories
values (1, 'StartUps');

insert into uni_categories
values (2, 'Tech');


insert into uni_categories
values (3, 'TEDxEvents');

insert into uni_categories
values (4, 'Uni');

insert into uni_postitions
values (1, 'Ads Management', 'We create and manage ads that you need, from creation to deployment. Lorem ipsum donor sit amet consicou.', '../../images/shield-icon.svg');

insert into uni_postitions
values (2, 'Video Marketing', 'Video marketing involves creating and sharing videos to promote a brand, product, or service to a target audience.', '../../images/support-icon.svg');

insert into uni_postitions
values (3, 'Customer Relation', 'Customer relation is the process of building and maintaining positive relationships with customers to enhance loyalty and satisfaction.', '../../images/customize-icon.svg');

insert into uni_postitions
values (4, 'Product Outreach', 'Product outreach refers to the process of promoting a product to a new or existing target audience to increase awareness and sales.', '../../images/reliable-icon.svg');

insert into uni_postitions
values (5, 'PR Campaign', 'A PR campaign is a planned effort to create and maintain a positive public image and reputation for a company or individual through media coverage.', '../../images/fast-icon.svg');

insert into uni_postitions
values (6, 'Product Expansion', 'Product expansion is the process of developing and introducing new products or features to an existing product line to increase revenue and market share.', '../../images/simple-icon.svg');


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


