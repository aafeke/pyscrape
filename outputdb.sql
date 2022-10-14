--
-- PostgreSQL database dump
--

-- Dumped from database version 13.8
-- Dumped by pg_dump version 13.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: tweet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tweet (
    id bigint NOT NULL,
    text character varying,
    created_at timestamp without time zone,
    author_id character varying
);


ALTER TABLE public.tweet OWNER TO postgres;

--
-- Data for Name: tweet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tweet (id, text, created_at, author_id) FROM stdin;
1580043398974562304	#ApplicationReceived\n#TwitterAPI\nI applied for being a #TwitterDev and my #ApplicationReceived! I hope I get approved. https://t.co/b1LsOs6KUE	2022-10-12 03:51:16	1460431590455414785
1580036138106245120	RT @_kato_shinya: #twitter_api_v2 is ready to take things to the next level. This library can be even more amazing :)\n\n#Programming #Dart #…	2022-10-12 03:22:25	1059961925948317702
\.


--
-- Name: tweet tweet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tweet
    ADD CONSTRAINT tweet_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

