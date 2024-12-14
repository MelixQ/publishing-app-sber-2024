--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application (
    id integer NOT NULL,
    genre character varying NOT NULL,
    target_audience_age integer NOT NULL,
    is_18 boolean NOT NULL,
    full_name character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying NOT NULL,
    socials character varying,
    submit_file_link character varying NOT NULL
);


ALTER TABLE public.application OWNER TO postgres;

--
-- Name: application_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.application_id_seq OWNER TO postgres;

--
-- Name: application_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_id_seq OWNED BY public.application.id;


--
-- Name: author; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.author (
    name character varying NOT NULL,
    info character varying,
    quotes character varying,
    id integer NOT NULL
);


ALTER TABLE public.author OWNER TO postgres;

--
-- Name: author_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.author_id_seq OWNER TO postgres;

--
-- Name: author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.author_id_seq OWNED BY public.author.id;


--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    title character varying NOT NULL,
    genre character varying NOT NULL,
    page_count integer NOT NULL,
    store_link character varying NOT NULL,
    picture character varying,
    id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.book OWNER TO postgres;

--
-- Name: book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.book_id_seq OWNER TO postgres;

--
-- Name: book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.book_id_seq OWNED BY public.book.id;


--
-- Name: application id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application ALTER COLUMN id SET DEFAULT nextval('public.application_id_seq'::regclass);


--
-- Name: author id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.author ALTER COLUMN id SET DEFAULT nextval('public.author_id_seq'::regclass);


--
-- Name: book id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book ALTER COLUMN id SET DEFAULT nextval('public.book_id_seq'::regclass);


--
-- Data for Name: application; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application (id, genre, target_audience_age, is_18, full_name, email, phone, socials, submit_file_link) FROM stdin;
2	╨г╨╢╨░╤Б╤Л	20	t	Kuznetsov Maxim Dmitrievich	email@email.com	+78005553535	@melix42	https://www.ozon.ru/product/kak-parovozik-pyhtelkin-pobedil-drakona-linitskiy-pavel-1335366025/
\.


--
-- Data for Name: author; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.author (name, info, quotes, id) FROM stdin;
╨Р╨╗╨╡╨║╤Б╨░╨╜╨┤╤А ╨б╨╡╤А╨│╨╡╨╡╨▓╨╕╤З ╨Я╤Г╤И╨║╨╕╨╜	╨а╤Г╤Б╤Б╨║╨╕╨╣ ╨┐╨╛╤Н╤В, ╨┤╤А╨░╨╝╨░╤В╤Г╤А╨│ ╨╕ ╨┐╤А╨╛╨╖╨░╨╕╨║, ╨╖╨░╨╗╨╛╨╢╨╕╨▓╤И╨╕╨╣ ╨╛╤Б╨╜╨╛╨▓╤Л ╤А╤Г╤Б╤Б╨║╨╛╨│╨╛ ╤А╨╡╨░╨╗╨╕╤Б╤В╨╕╤З╨╡╤Б╨║╨╛╨│╨╛ ╨╜╨░╨┐╤А╨░╨▓╨╗╨╡╨╜╨╕╤П, ╨╗╨╕╤В╨╡╤А╨░╤В╤Г╤А╨╜╤Л╨╣ ╨║╤А╨╕╤В╨╕╨║ ╨╕ ╤В╨╡╨╛╤А╨╡╤В╨╕╨║ ╨╗╨╕╤В╨╡╤А╨░╤В╤Г╤А╤Л, ╨╕╤Б╤В╨╛╤А╨╕╨║, ╨┐╤Г╨▒╨╗╨╕╤Ж╨╕╤Б╤В, ╨╢╤Г╤А╨╜╨░╨╗╨╕╤Б╤В, ╤А╨╡╨┤╨░╨║╤В╨╛╤А ╨╕ ╨╕╨╖╨┤╨░╤В╨╡╨╗╤М. ╨Ю╨┤╨╕╨╜ ╨╕╨╖ ╤Б╨░╨╝╤Л╤Е ╨░╨▓╤В╨╛╤А╨╕╤В╨╡╤В╨╜╤Л╤Е ╨╗╨╕╤В╨╡╤А╨░╤В╤Г╤А╨╜╤Л╤Е ╨┤╨╡╤П╤В╨╡╨╗╨╡╨╣ ╨┐╨╡╤А╨▓╨╛╨╣ ╤В╤А╨╡╤В╨╕ XIX ╨▓╨╡╨║╨░	╨У╨┤╨╡ ╨╜╨╡╤В ╨╗╤О╨▒╨▓╨╕ ╨║ ╨╕╤Б╨║╤Г╤Б╤Б╤В╨▓╤Г, ╤В╨░╨╝ ╨╜╨╡╤В ╨╕ ╨║╤А╨╕╤В╨╕╨║╨╕	1
╨Ь╨╕╤Е╨░╨╕╨╗ ╨о╤А╤М╨╡╨▓╨╕╤З ╨Ы╨╡╤А╨╝╨╛╨╜╤В╨╛╨▓	╨а╤Г╤Б╤Б╨║╨╕╨╣ ╨┐╨╛╤Н╤В, ╨┐╤А╨╛╨╖╨░╨╕╨║, ╨┤╤А╨░╨╝╨░╤В╤Г╤А╨│, ╤Е╤Г╨┤╨╛╨╢╨╜╨╕╨║. ╨Я╨╛╤А╤Г╤З╨╕╨║ ╨╗╨╡╨╣╨▒-╨│╨▓╨░╤А╨┤╨╕╨╕ ╨У╤Г╤Б╨░╤А╤Б╨║╨╛╨│╨╛ ╨┐╨╛╨╗╨║╨░	╨а╨░╨┤╨╛╤Б╤В╨╕ ╨╖╨░╨▒╤Л╨▓╨░╤О╤В╤Б╤П, ╨░ ╨┐╨╡╤З╨░╨╗╨╕ ╨╜╨╕╨║╨╛╨│╨┤╨░.	2
\.


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book (title, genre, page_count, store_link, picture, id, author_id) FROM stdin;
╨б╨║╨░╨╖╨║╨╕ ╨Ы╤Г╨║╨╛╨╝╨╛╤А╤М╤П 2	╨б╨║╨░╨╖╨║╨╕	96	https://www.ozon.ru/product/skazki-lukomorya-pushkin-aleksandr-sergeevich-1231142288/		2	2
\.


--
-- Name: application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_id_seq', 2, true);


--
-- Name: author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.author_id_seq', 4, true);


--
-- Name: book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.book_id_seq', 2, true);


--
-- Name: application application_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pkey PRIMARY KEY (id);


--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);


--
-- Name: book book_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.author(id);


--
-- Name: TABLE application; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.application TO PUBLIC;


--
-- Name: TABLE author; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.author TO PUBLIC;


--
-- Name: TABLE book; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.book TO PUBLIC;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES TO PUBLIC;


--
-- PostgreSQL database dump complete
--

