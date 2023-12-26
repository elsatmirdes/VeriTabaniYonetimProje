--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 16.0

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

--
-- Name: Personel; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "Personel";


ALTER SCHEMA "Personel" OWNER TO postgres;

--
-- Name: manOlusturPersonel(character varying, character varying, character varying, timestamp without time zone, integer, character varying, character varying, bigint); Type: FUNCTION; Schema: Personel; Owner: postgres
--

CREATE FUNCTION "Personel"."manOlusturPersonel"(ad character varying, soyad character varying, email character varying, tarih timestamp without time zone, maas integer, phone character varying, pertip character varying, tc bigint) RETURNS void
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
BEGIN   
    -- Rastgele bilgilerle Personel tablosuna ekleme
    INSERT INTO "Personel"."Personel" ("adi", "soyadi", "email", "kayittarihi", "maas", "phoneNumber", "personelTipi","tcKimlik") 
    VALUES(
        ad,
        soyad,
        email,
        tarih,
        maas,
        phone,
        perTip,
        tc
    );

    -- Eğer tip "D" ise, Driver tablosuna da ekleyin
    IF perTip = 'D' THEN
        INSERT INTO "Personel"."Driver" ("personelNo", "sirket") 
        VALUES (
            currval(pg_get_serial_sequence('"Personel"."Personel"', 'personelNo')),
            'Mirdes Tic. Ltd. Şti.'
        );
    ELSE
        --  Eğer tip "D" değilse, vasifsizPer tablosuna ekleme
        INSERT INTO "Personel"."vasifsizPer" ("personelNo","sirket") 
        VALUES (
            currval(pg_get_serial_sequence('"Personel"."Personel"', 'personelNo')),'Mirdes Tic. Ltd. Şti.'
        );
    END IF;
END;
$$;


ALTER FUNCTION "Personel"."manOlusturPersonel"(ad character varying, soyad character varying, email character varying, tarih timestamp without time zone, maas integer, phone character varying, pertip character varying, tc bigint) OWNER TO postgres;

--
-- Name: olusturPersonel(integer); Type: FUNCTION; Schema: Personel; Owner: postgres
--

CREATE FUNCTION "Personel"."olusturPersonel"(kayitsayisi integer) RETURNS void
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE
    isimler VARCHAR[] := ARRAY['Ali', 'Ayşe', 'Mustafa', 'Fatma', 'Mehmet', 'Zeynep', 'Emre', 'Elif', 'Ahmet', 'Hülya'];
    soyadlar VARCHAR[] := ARRAY['Yılmaz', 'Kaya', 'Demir', 'Çelik', 'Güler', 'Aydın', 'Kurt', 'Öztürk', 'Yıldız', 'Aksoy'];
    emails VARCHAR[] := ARRAY['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'];
    tip CHAR := 'M';
BEGIN   
    IF kayitSayisi > 0 THEN
        FOR i IN 1 .. kayitSayisi LOOP
            -- Rastgele olarak "M" veya "D" tipinde personel seçme
            tip := CASE WHEN random() < 0.5 THEN 'M' ELSE 'D' END;
            
            -- Rastgele bilgilerle Personel tablosuna ekleme
            INSERT INTO "Personel"."Personel" ("adi", "soyadi", "email", "kayittarihi", "maas", "phoneNumber", "personelTipi") 
            VALUES(
                isimler[ceil(random() * array_length(isimler, 1))],
                soyadlar[ceil(random() * array_length(soyadlar, 1))],
                isimler[ceil(random() * array_length(isimler, 1))] || '.' || soyadlar[ceil(random() * array_length(soyadlar, 1))] || '@' || emails[ceil(random() *                 array_length(emails, 1))],
                NOW() + (random() * (NOW() + '365 days' - NOW())),
                random() * 10000 + 2000,
                '+90 ' || floor(random() * 5000000000 + 5888888888)::BIGINT::VARCHAR,
                tip
            );

            -- Eğer tip "D" ise, Driver tablosuna da ekleyin
            IF tip = 'D' THEN
                INSERT INTO "Personel"."Driver" ("personelNo", "sirket") 
                VALUES (
                    currval(pg_get_serial_sequence('"Personel"."Personel"', 'personelNo')),
                    'Mirdes Tic. Ltd. Şti.'
                );
            ELSE
            --  Eğer tip "D" değilse, vasifsizPer tablosuna ekleme
                INSERT INTO "Personel"."vasifsizPer" ("personelNo",sirket) 
                VALUES (
                    currval(pg_get_serial_sequence('"Personel"."Personel"', 'personelNo')),'Mirdes Tic. Ltd. Şti.'
                );
            END IF;
        END LOOP;
    END IF; 
END;
$$;


ALTER FUNCTION "Personel"."olusturPersonel"(kayitsayisi integer) OWNER TO postgres;

--
-- Name: silPersonel(bigint); Type: PROCEDURE; Schema: Personel; Owner: postgres
--

CREATE PROCEDURE "Personel"."silPersonel"(IN tckimlikno bigint)
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
 BEGIN
	 
	 DELETE FROM "Personel"."Personel" WHERE "tcKimlik"=tcKimlikNo;
	 
END;
$$;


ALTER PROCEDURE "Personel"."silPersonel"(IN tckimlikno bigint) OWNER TO postgres;

--
-- Name: kontrol_bilet(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.kontrol_bilet() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Eğer sefer ve çalışan zaten kayıtlıysa, eklemeyi engelle
    IF EXISTS (
        SELECT *
        FROM "Bilet"
        WHERE "customerID" = NEW."customerID" AND "seferPrID" = NEW."seferPrID"
    ) THEN
        
        RAISE EXCEPTION 'Bu sefer programı zaten oluşturulmuş';
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.kontrol_bilet() OWNER TO postgres;

--
-- Name: kontrol_calisanprogrami(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.kontrol_calisanprogrami() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Eğer sefer ve çalışan zaten kayıtlıysa, eklemeyi engelle
    IF EXISTS (
        SELECT *
        FROM "calisanProgrami"
        WHERE "seferProgrami" = NEW."seferProgrami" AND "calisan" = NEW."calisan"
    ) THEN
        
        RAISE EXCEPTION 'Bu sefer ve çalışan zaten kayıtlı!';
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.kontrol_calisanprogrami() OWNER TO postgres;

--
-- Name: kontrol_otobus(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.kontrol_otobus() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Eğer sefer ve çalışan zaten kayıtlıysa, eklemeyi engelle
    IF EXISTS (
        SELECT *
        FROM "Otobus"
        WHERE "Plaka" = NEW."Plaka"
    ) THEN
        
        RAISE EXCEPTION 'Bu otobüs zaten kayıtlı!';
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.kontrol_otobus() OWNER TO postgres;

--
-- Name: kontrol_seferprogrami(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.kontrol_seferprogrami() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Eğer sefer ve çalışan zaten kayıtlıysa, eklemeyi engelle
    IF EXISTS (
        SELECT *
        FROM "SeferProgrami"
        WHERE "hareketSaati" = NEW."hareketSaati" AND "otobus" = NEW."otobus"
    ) THEN
        
        RAISE EXCEPTION 'Bu sefer programı zaten oluşturulmuş';
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.kontrol_seferprogrami() OWNER TO postgres;

--
-- Name: olusturotobus(integer, character varying, character varying, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.olusturotobus(koltuksay integer, marka character varying, model character varying, plaka character varying) RETURNS void
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
BEGIN   
    -- Rastgele bilgilerle Otobus tablosuna ekleme
    INSERT INTO "Otobus" ("koltukSayisi", "Marka", "Model", "Plaka") 
    VALUES (
        koltuksay,
        marka,
        model,
        plaka
    );
END;
$$;


ALTER FUNCTION public.olusturotobus(koltuksay integer, marka character varying, model character varying, plaka character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Driver; Type: TABLE; Schema: Personel; Owner: postgres
--

CREATE TABLE "Personel"."Driver" (
    "personelNo" integer NOT NULL,
    sirket character varying(40) NOT NULL
);


ALTER TABLE "Personel"."Driver" OWNER TO postgres;

--
-- Name: Personel; Type: TABLE; Schema: Personel; Owner: postgres
--

CREATE TABLE "Personel"."Personel" (
    "personelNo" integer NOT NULL,
    adi character varying(40) NOT NULL,
    soyadi character varying(40) NOT NULL,
    maas integer,
    "phoneNumber" character(30),
    email character varying(40),
    "personelTipi" character(1) NOT NULL,
    kayittarihi timestamp with time zone,
    "tcKimlik" bigint
);


ALTER TABLE "Personel"."Personel" OWNER TO postgres;

--
-- Name: Personel_personelNo_seq; Type: SEQUENCE; Schema: Personel; Owner: postgres
--

CREATE SEQUENCE "Personel"."Personel_personelNo_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE "Personel"."Personel_personelNo_seq" OWNER TO postgres;

--
-- Name: Personel_personelNo_seq; Type: SEQUENCE OWNED BY; Schema: Personel; Owner: postgres
--

ALTER SEQUENCE "Personel"."Personel_personelNo_seq" OWNED BY "Personel"."Personel"."personelNo";


--
-- Name: vasifsizPer; Type: TABLE; Schema: Personel; Owner: postgres
--

CREATE TABLE "Personel"."vasifsizPer" (
    "personelNo" integer NOT NULL,
    sirket character varying(40) NOT NULL
);


ALTER TABLE "Personel"."vasifsizPer" OWNER TO postgres;

--
-- Name: Bilet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Bilet" (
    "TicketID" integer NOT NULL,
    "customerID" integer,
    "seferPrID" integer,
    "koltukNO" integer,
    fiyat integer,
    "SatinalmaTarihi" timestamp without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone
);


ALTER TABLE public."Bilet" OWNER TO postgres;

--
-- Name: Bilet_TicketID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Bilet_TicketID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Bilet_TicketID_seq" OWNER TO postgres;

--
-- Name: Bilet_TicketID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Bilet_TicketID_seq" OWNED BY public."Bilet"."TicketID";


--
-- Name: Musteri; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Musteri" (
    "CustomerID" integer NOT NULL,
    adi character varying(40),
    soyadi character varying(40) NOT NULL,
    "phoneNumber" bigint NOT NULL,
    email character varying(40),
    "tcKimlik" bigint
);


ALTER TABLE public."Musteri" OWNER TO postgres;

--
-- Name: Musteri_CustomerID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Musteri_CustomerID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Musteri_CustomerID_seq" OWNER TO postgres;

--
-- Name: Musteri_CustomerID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Musteri_CustomerID_seq" OWNED BY public."Musteri"."CustomerID";


--
-- Name: Odeme; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Odeme" (
    "odemeID" integer NOT NULL,
    "ticketID" integer,
    "odemeTarihi" timestamp without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone,
    "odemeTipi" character(20)
);


ALTER TABLE public."Odeme" OWNER TO postgres;

--
-- Name: Odeme_odemeID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Odeme_odemeID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Odeme_odemeID_seq" OWNER TO postgres;

--
-- Name: Odeme_odemeID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Odeme_odemeID_seq" OWNED BY public."Odeme"."odemeID";


--
-- Name: Otobus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Otobus" (
    "BusID" integer NOT NULL,
    "Plaka" character varying(15) NOT NULL,
    "Marka" character varying(40),
    "Model" character varying(20),
    "koltukSayisi" integer NOT NULL
);


ALTER TABLE public."Otobus" OWNER TO postgres;

--
-- Name: Otobus_BusID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Otobus_BusID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Otobus_BusID_seq" OWNER TO postgres;

--
-- Name: Otobus_BusID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Otobus_BusID_seq" OWNED BY public."Otobus"."BusID";


--
-- Name: Promosyon; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Promosyon" (
    "promosyonID" integer NOT NULL,
    "promoKodu" character varying(10),
    "promosyonYuzdesi" integer NOT NULL,
    tanim character varying(60)
);


ALTER TABLE public."Promosyon" OWNER TO postgres;

--
-- Name: Promosyon_promosyonID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Promosyon_promosyonID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Promosyon_promosyonID_seq" OWNER TO postgres;

--
-- Name: Promosyon_promosyonID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Promosyon_promosyonID_seq" OWNED BY public."Promosyon"."promosyonID";


--
-- Name: Reklam; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Reklam" (
    "reklamID" integer NOT NULL,
    "reklamBaslik" character varying(10),
    "reklamIcerigi" character varying(60),
    "baslangıcTarihi" timestamp without time zone,
    "bitisTarihi" timestamp without time zone
);


ALTER TABLE public."Reklam" OWNER TO postgres;

--
-- Name: Reklam_reklamID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Reklam_reklamID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Reklam_reklamID_seq" OWNER TO postgres;

--
-- Name: Reklam_reklamID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Reklam_reklamID_seq" OWNED BY public."Reklam"."reklamID";


--
-- Name: Sefer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Sefer" (
    "SeferID" integer NOT NULL,
    "Kalkıs" character varying(30),
    "Varıs" character varying(30),
    "KalkısTarih" date DEFAULT '2019-01-01 01:00:00'::timestamp without time zone,
    "VarisTarihi" date DEFAULT '2019-01-01 01:00:00'::timestamp without time zone
);


ALTER TABLE public."Sefer" OWNER TO postgres;

--
-- Name: SeferProgrami; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SeferProgrami" (
    "seferProgramID" integer NOT NULL,
    sefer integer NOT NULL,
    otobus integer NOT NULL,
    "hareketSaati" time without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone,
    "varisSaati" time without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone,
    "Fiyat" integer
);


ALTER TABLE public."SeferProgrami" OWNER TO postgres;

--
-- Name: SeferProgrami_seferProgramID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SeferProgrami_seferProgramID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."SeferProgrami_seferProgramID_seq" OWNER TO postgres;

--
-- Name: SeferProgrami_seferProgramID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SeferProgrami_seferProgramID_seq" OWNED BY public."SeferProgrami"."seferProgramID";


--
-- Name: Sefer_SeferID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Sefer_SeferID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Sefer_SeferID_seq" OWNER TO postgres;

--
-- Name: Sefer_SeferID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Sefer_SeferID_seq" OWNED BY public."Sefer"."SeferID";


--
-- Name: bilet_ticketid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bilet_ticketid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.bilet_ticketid_seq OWNER TO postgres;

--
-- Name: calisanProgrami; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."calisanProgrami" (
    "calisanProgramiID" integer NOT NULL,
    calisan integer,
    "seferProgrami" integer
);


ALTER TABLE public."calisanProgrami" OWNER TO postgres;

--
-- Name: calisanProgrami_calisanProgramiID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."calisanProgrami_calisanProgramiID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."calisanProgrami_calisanProgramiID_seq" OWNER TO postgres;

--
-- Name: calisanProgrami_calisanProgramiID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."calisanProgrami_calisanProgramiID_seq" OWNED BY public."calisanProgrami"."calisanProgramiID";


--
-- Name: geriBildirim; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."geriBildirim" (
    "geriBilfirimID" integer NOT NULL,
    musteri integer NOT NULL,
    sefer integer NOT NULL,
    degerlendirme integer NOT NULL,
    yorum character varying(100),
    CONSTRAINT "geriBildirim_degerlendirme_check" CHECK (((degerlendirme >= 1) AND (degerlendirme <= 10)))
);


ALTER TABLE public."geriBildirim" OWNER TO postgres;

--
-- Name: geriBildirim_geriBilfirimID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."geriBildirim_geriBilfirimID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."geriBildirim_geriBilfirimID_seq" OWNER TO postgres;

--
-- Name: geriBildirim_geriBilfirimID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."geriBildirim_geriBilfirimID_seq" OWNED BY public."geriBildirim"."geriBilfirimID";


--
-- Name: indirim; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.indirim (
    "indirimID" integer NOT NULL,
    "indirimKodu" character varying(10),
    "indirimYuzdesi" integer NOT NULL,
    "sonKullanmaTarihi" timestamp without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone
);


ALTER TABLE public.indirim OWNER TO postgres;

--
-- Name: indirim_indirimID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."indirim_indirimID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."indirim_indirimID_seq" OWNER TO postgres;

--
-- Name: indirim_indirimID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."indirim_indirimID_seq" OWNED BY public.indirim."indirimID";


--
-- Name: otobusbakim_bakimid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.otobusbakim_bakimid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.otobusbakim_bakimid_seq OWNER TO postgres;

--
-- Name: otobusBakim; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."otobusBakim" (
    "bakimID" integer DEFAULT nextval('public.otobusbakim_bakimid_seq'::regclass) NOT NULL,
    "busID" integer NOT NULL,
    "bakimTarihi" timestamp without time zone DEFAULT '2019-01-01 01:00:00'::timestamp without time zone,
    aciklama character varying(100) NOT NULL
);


ALTER TABLE public."otobusBakim" OWNER TO postgres;

--
-- Name: otobus_otobusid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.otobus_otobusid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.otobus_otobusid_seq OWNER TO postgres;

--
-- Name: Personel personelNo; Type: DEFAULT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."Personel" ALTER COLUMN "personelNo" SET DEFAULT nextval('"Personel"."Personel_personelNo_seq"'::regclass);


--
-- Name: Bilet TicketID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Bilet" ALTER COLUMN "TicketID" SET DEFAULT nextval('public."Bilet_TicketID_seq"'::regclass);


--
-- Name: Musteri CustomerID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Musteri" ALTER COLUMN "CustomerID" SET DEFAULT nextval('public."Musteri_CustomerID_seq"'::regclass);


--
-- Name: Odeme odemeID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Odeme" ALTER COLUMN "odemeID" SET DEFAULT nextval('public."Odeme_odemeID_seq"'::regclass);


--
-- Name: Otobus BusID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Otobus" ALTER COLUMN "BusID" SET DEFAULT nextval('public."Otobus_BusID_seq"'::regclass);


--
-- Name: Promosyon promosyonID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Promosyon" ALTER COLUMN "promosyonID" SET DEFAULT nextval('public."Promosyon_promosyonID_seq"'::regclass);


--
-- Name: Reklam reklamID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Reklam" ALTER COLUMN "reklamID" SET DEFAULT nextval('public."Reklam_reklamID_seq"'::regclass);


--
-- Name: Sefer SeferID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Sefer" ALTER COLUMN "SeferID" SET DEFAULT nextval('public."Sefer_SeferID_seq"'::regclass);


--
-- Name: SeferProgrami seferProgramID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SeferProgrami" ALTER COLUMN "seferProgramID" SET DEFAULT nextval('public."SeferProgrami_seferProgramID_seq"'::regclass);


--
-- Name: calisanProgrami calisanProgramiID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."calisanProgrami" ALTER COLUMN "calisanProgramiID" SET DEFAULT nextval('public."calisanProgrami_calisanProgramiID_seq"'::regclass);


--
-- Name: geriBildirim geriBilfirimID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."geriBildirim" ALTER COLUMN "geriBilfirimID" SET DEFAULT nextval('public."geriBildirim_geriBilfirimID_seq"'::regclass);


--
-- Name: indirim indirimID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.indirim ALTER COLUMN "indirimID" SET DEFAULT nextval('public."indirim_indirimID_seq"'::regclass);


--
-- Data for Name: Driver; Type: TABLE DATA; Schema: Personel; Owner: postgres
--

INSERT INTO "Personel"."Driver" VALUES
	(11, 'Mirdes Tic. Ltd. Şti.'),
	(14, 'Mirdes Tic. Ltd. Şti.'),
	(16, 'Mirdes Tic. Ltd. Şti.'),
	(29, 'Mirdes Tic. Ltd. Şti.'),
	(21, 'Mirdes Tic. Ltd. Şti.');


--
-- Data for Name: Personel; Type: TABLE DATA; Schema: Personel; Owner: postgres
--

INSERT INTO "Personel"."Personel" VALUES
	(11, 'Emre', 'Demir', 5301, '+90 10805854786               ', 'Ali.Aydın@hotmail.com', 'D', '2024-07-04 22:33:02.169376+00', 34658975124),
	(12, 'Ali', 'Demir', 5395, '+90 6463007287                ', 'Ali.Aksoy@hotmail.com', 'M', '2024-05-07 21:03:37.038831+00', 13254678945),
	(13, 'Zeynep', 'Kurt', 10508, '+90 9562296923                ', 'Ayşe.Çelik@outlook.com', 'M', '2024-03-12 22:05:08.670972+00', 26587465312),
	(14, 'Ayşe', 'Demir', 11977, '+90 8525144121                ', 'Ahmet.Öztürk@yahoo.com', 'D', '2024-03-27 08:48:20.857419+00', 96542356870),
	(15, 'Mustafa', 'Kaya', 2100, '+90 9340128355                ', 'Mehmet.Aydın@hotmail.com', 'M', '2023-12-29 18:00:37.649873+00', 46791346798),
	(16, 'Mehmet', 'Aksoy', 10940, '+90 6424548658                ', 'Elif.Aksoy@yahoo.com', 'D', '2024-09-28 09:49:44.657191+00', 46856923512),
	(18, 'Emre', 'Aydın', 6470, '+90 10790776076               ', 'Hülya.Kaya@hotmail.com', 'M', '2024-06-14 06:15:18.191114+00', 85465365486),
	(19, 'Mehmet', 'Kaya', 11984, '+90 6820475465                ', 'Fatma.Aydın@hotmail.com', 'M', '2024-10-18 18:49:16.840094+00', 16458732502),
	(17, 'Zeynep', 'Yılmaz', 16454, '5364875687                    ', 'zeynep@gmail.com', 'M', '2024-02-02 09:57:48.251078+00', 76453146836),
	(29, 'Osman', 'Yıldız', 46700, '5446247475                    ', 'yildiz03032004@hotmail.com', 'D', '2023-12-12 00:00:00+00', 1548765978),
	(30, 'Abdulsamet', 'dryhoney', 25000, '534665987                     ', 'samet@gmail.com', 'M', '2023-12-12 00:00:00+00', 25469875632),
	(21, 'ELSAT', 'MIRDES', 45687, '5388415603                    ', 'elsat@gmail.com', 'D', '2023-12-05 00:00:00+00', 47866956034),
	(32, 'OZCAN', 'DEMIRCI', 22500, '5394275304                    ', 'OZCAN@GMAİL.COM', 'S', '2023-12-17 00:00:00+00', 98778894587),
	(34, 'dilan', 'polat', 5456, '5425487547                    ', 'dilan@hotmail.com', 'V', '2023-12-25 00:00:00+00', 65987452145);


--
-- Data for Name: vasifsizPer; Type: TABLE DATA; Schema: Personel; Owner: postgres
--



--
-- Data for Name: Bilet; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Bilet" VALUES
	(2, 11, 7, 9, 270, '2023-12-16 00:00:00'),
	(6, 13, 2, 13, 350, '2023-12-16 00:00:00'),
	(7, 14, 8, 7, 280, '2023-12-16 00:00:00'),
	(8, 15, 10, 26, 285, '2023-12-16 00:00:00'),
	(9, 16, 7, 6, 270, '2023-12-16 00:00:00'),
	(11, 17, 11, 10, 299, '2023-12-17 00:00:00'),
	(12, 18, 12, 1, 217, '2023-12-25 00:00:00'),
	(15, 19, 7, 5, 270, '2023-12-26 00:00:00'),
	(19, 20, 7, 8, 189, '2023-12-26 00:00:00');


--
-- Data for Name: Musteri; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Musteri" VALUES
	(11, 'elsat', 'mir', 538415603, 'elsatgmail.com', 47866956034),
	(12, 'timur', 'mirdes', 5348474, 'timur@gmail.com', 4785786),
	(13, 'ayşe', 'mir', 5511015428, 'ayse@gmail.com', 47875955752),
	(14, 'nefise', 'mir', 5358475987, 'nefise@gmail.com', 47855984757),
	(15, 'CAN', 'MİRDES', 5348474777, 'can@gmail.com', 47878998745),
	(16, 'ozcan', 'gafurov', 5394275304, 'ozcan@gmail.com', 9907899777),
	(17, 'ozcan', 'demirci', 5394275304, 'ozcan@gmail.com', 98778894587),
	(18, 'Yigit', 'acar', 5374171716, 'yigitacar@hotmail.com', 18642838462),
	(19, 'salih', 'yalın', 5388415603, 'elsat_mird@hotmail.com', 58766452314),
	(20, 'canan', 'karatay', 5445545545, 'cana@gmail.com', 11225544778);


--
-- Data for Name: Odeme; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Odeme" VALUES
	(1, 11, '2023-12-17 00:00:00', 'Kredi Kartı         '),
	(2, 12, '2023-12-25 00:00:00', 'Kredi Kartı         '),
	(3, 15, '2023-12-26 00:00:00', 'Nakit               '),
	(5, 19, '2023-12-26 00:00:00', 'Nakit               ');


--
-- Data for Name: Otobus; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Otobus" VALUES
	(1, '34 FK 5416', 'Mercedes', '2016 Benz', 52),
	(2, '46 GS 1905', 'Mercedes', 'Benz', 52),
	(4, '56 AS 001', 'Mercedes', 'Benz', 26),
	(6, '16 KDC 61', 'BCI', 'Range', 45),
	(7, '16 EM 16', 'Güleryüz', '02', 35),
	(8, '77 SFG 1564', 'KARSAN', 'C2', 46),
	(9, '08 SMH 27', 'SECKİN', '2023', 46),
	(10, '34 VRT 54', 'MERCEDES', 'BENZ', 52),
	(13, '34 VRT 53', 'MERCEDES', 'BENZ', 34);


--
-- Data for Name: Promosyon; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Promosyon" VALUES
	(1, 'asde4s', 15, 'çalışanlara');


--
-- Data for Name: Reklam; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: Sefer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Sefer" VALUES
	(3, 'SAKARYA', 'BURSA', '2023-12-12', '2023-12-13'),
	(4, 'ANKARA', 'ORDU', '2023-12-20', '2023-12-20'),
	(1, 'BURSA', 'SAKARYA', '2023-12-15', '2023-12-15'),
	(5, 'AĞRI', 'DİYARBAKIR', '2023-12-25', '2023-12-25'),
	(8, 'BURSA', 'SAKARYA', '2023-12-16', '2023-12-16'),
	(9, 'SAKARYA', 'BURSA', '2023-12-26', '2023-12-26');


--
-- Data for Name: SeferProgrami; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."SeferProgrami" VALUES
	(1, 3, 2, '15:30:00', '18:25:00', 290),
	(2, 4, 4, '01:15:00', '06:30:00', 350),
	(4, 5, 7, '12:30:00', '17:30:00', 400),
	(6, 1, 4, '12:30:00', '15:15:00', 250),
	(7, 1, 2, '08:30:00', '11:45:00', 270),
	(8, 4, 1, '15:30:00', '19:50:00', 400),
	(9, 4, 7, '18:15:00', '23:15:00', 400),
	(10, 1, 8, '17:50:00', '20:30:00', 285),
	(11, 8, 8, '16:45:00', '18:30:00', 299),
	(12, 9, 9, '16:15:00', '18:30:00', 310),
	(13, 5, 7, '15:00:00', '20:00:00', 320),
	(15, 5, 10, '09:30:00', '14:30:00', 320);


--
-- Data for Name: calisanProgrami; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."calisanProgrami" VALUES
	(3, 11, 1),
	(17, 11, 8);


--
-- Data for Name: geriBildirim; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: indirim; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.indirim VALUES
	(1, 'z4aws', 30, '2024-10-05 12:10:00');


--
-- Data for Name: otobusBakim; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."otobusBakim" VALUES
	(1, 10, '2023-12-26 00:00:00', 'rutin kontrol');


--
-- Name: Personel_personelNo_seq; Type: SEQUENCE SET; Schema: Personel; Owner: postgres
--

SELECT pg_catalog.setval('"Personel"."Personel_personelNo_seq"', 35, true);


--
-- Name: Bilet_TicketID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Bilet_TicketID_seq"', 20, true);


--
-- Name: Musteri_CustomerID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Musteri_CustomerID_seq"', 20, true);


--
-- Name: Odeme_odemeID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Odeme_odemeID_seq"', 5, true);


--
-- Name: Otobus_BusID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Otobus_BusID_seq"', 14, true);


--
-- Name: Promosyon_promosyonID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Promosyon_promosyonID_seq"', 1, true);


--
-- Name: Reklam_reklamID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Reklam_reklamID_seq"', 1, false);


--
-- Name: SeferProgrami_seferProgramID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SeferProgrami_seferProgramID_seq"', 16, true);


--
-- Name: Sefer_SeferID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Sefer_SeferID_seq"', 9, true);


--
-- Name: bilet_ticketid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bilet_ticketid_seq', 2, true);


--
-- Name: calisanProgrami_calisanProgramiID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."calisanProgrami_calisanProgramiID_seq"', 21, true);


--
-- Name: geriBildirim_geriBilfirimID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."geriBildirim_geriBilfirimID_seq"', 1, false);


--
-- Name: indirim_indirimID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."indirim_indirimID_seq"', 1, true);


--
-- Name: otobus_otobusid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.otobus_otobusid_seq', 1, false);


--
-- Name: otobusbakim_bakimid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.otobusbakim_bakimid_seq', 1, true);


--
-- Name: Driver Driver_pkey; Type: CONSTRAINT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."Driver"
    ADD CONSTRAINT "Driver_pkey" PRIMARY KEY ("personelNo");


--
-- Name: Personel personelPK; Type: CONSTRAINT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."Personel"
    ADD CONSTRAINT "personelPK" PRIMARY KEY ("personelNo");


--
-- Name: vasifsizPer vasifsizPer_pkey; Type: CONSTRAINT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."vasifsizPer"
    ADD CONSTRAINT "vasifsizPer_pkey" PRIMARY KEY ("personelNo");


--
-- Name: Promosyon PROMOSYONpk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Promosyon"
    ADD CONSTRAINT "PROMOSYONpk" PRIMARY KEY ("promosyonID");


--
-- Name: otobusBakim bakimPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."otobusBakim"
    ADD CONSTRAINT "bakimPK" PRIMARY KEY ("bakimID");


--
-- Name: Otobus busID; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Otobus"
    ADD CONSTRAINT "busID" PRIMARY KEY ("BusID");


--
-- Name: calisanProgrami calisanProgramiPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."calisanProgrami"
    ADD CONSTRAINT "calisanProgramiPK" PRIMARY KEY ("calisanProgramiID");


--
-- Name: Musteri cutomerPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Musteri"
    ADD CONSTRAINT "cutomerPK" PRIMARY KEY ("CustomerID");


--
-- Name: geriBildirim geriBildirimPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."geriBildirim"
    ADD CONSTRAINT "geriBildirimPK" PRIMARY KEY ("geriBilfirimID");


--
-- Name: indirim indirimPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.indirim
    ADD CONSTRAINT "indirimPK" PRIMARY KEY ("indirimID");


--
-- Name: Odeme odemePK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Odeme"
    ADD CONSTRAINT "odemePK" PRIMARY KEY ("odemeID");


--
-- Name: Reklam reklamPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Reklam"
    ADD CONSTRAINT "reklamPK" PRIMARY KEY ("reklamID");


--
-- Name: Sefer seferID; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Sefer"
    ADD CONSTRAINT "seferID" PRIMARY KEY ("SeferID");


--
-- Name: SeferProgrami seferProgramiPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SeferProgrami"
    ADD CONSTRAINT "seferProgramiPK" PRIMARY KEY ("seferProgramID");


--
-- Name: Bilet ticketPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Bilet"
    ADD CONSTRAINT "ticketPK" PRIMARY KEY ("TicketID");


--
-- Name: Bilet trigger_kontrol_bilet; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_kontrol_bilet BEFORE INSERT ON public."Bilet" FOR EACH ROW EXECUTE FUNCTION public.kontrol_bilet();


--
-- Name: calisanProgrami trigger_kontrol_calisanprogrami; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_kontrol_calisanprogrami BEFORE INSERT ON public."calisanProgrami" FOR EACH ROW EXECUTE FUNCTION public.kontrol_calisanprogrami();


--
-- Name: Otobus trigger_kontrol_otobus; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_kontrol_otobus BEFORE INSERT ON public."Otobus" FOR EACH ROW EXECUTE FUNCTION public.kontrol_otobus();


--
-- Name: SeferProgrami trigger_kontrol_seferprogrami; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trigger_kontrol_seferprogrami BEFORE INSERT ON public."SeferProgrami" FOR EACH ROW EXECUTE FUNCTION public.kontrol_seferprogrami();


--
-- Name: Driver driverPersonel; Type: FK CONSTRAINT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."Driver"
    ADD CONSTRAINT "driverPersonel" FOREIGN KEY ("personelNo") REFERENCES "Personel"."Personel"("personelNo") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: vasifsizPer vasifsizPerFK; Type: FK CONSTRAINT; Schema: Personel; Owner: postgres
--

ALTER TABLE ONLY "Personel"."vasifsizPer"
    ADD CONSTRAINT "vasifsizPerFK" FOREIGN KEY ("personelNo") REFERENCES "Personel"."Personel"("personelNo") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: otobusBakim busFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."otobusBakim"
    ADD CONSTRAINT "busFK" FOREIGN KEY ("busID") REFERENCES public."Otobus"("BusID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: calisanProgrami calisanFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."calisanProgrami"
    ADD CONSTRAINT "calisanFK" FOREIGN KEY (calisan) REFERENCES "Personel"."Personel"("personelNo");


--
-- Name: Bilet customerFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Bilet"
    ADD CONSTRAINT "customerFK" FOREIGN KEY ("customerID") REFERENCES public."Musteri"("CustomerID") ON DELETE CASCADE;


--
-- Name: geriBildirim musteriFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."geriBildirim"
    ADD CONSTRAINT "musteriFK" FOREIGN KEY (musteri) REFERENCES public."Musteri"("CustomerID");


--
-- Name: Odeme odemeBilFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Odeme"
    ADD CONSTRAINT "odemeBilFK" FOREIGN KEY ("ticketID") REFERENCES public."Bilet"("TicketID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: SeferProgrami otobusFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SeferProgrami"
    ADD CONSTRAINT "otobusFK" FOREIGN KEY (otobus) REFERENCES public."Otobus"("BusID");


--
-- Name: geriBildirim seferBilFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."geriBildirim"
    ADD CONSTRAINT "seferBilFK" FOREIGN KEY (sefer) REFERENCES public."Sefer"("SeferID");


--
-- Name: SeferProgrami seferFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SeferProgrami"
    ADD CONSTRAINT "seferFK" FOREIGN KEY (sefer) REFERENCES public."Sefer"("SeferID");


--
-- Name: SeferProgrami seferFK3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SeferProgrami"
    ADD CONSTRAINT "seferFK3" FOREIGN KEY (sefer) REFERENCES public."Sefer"("SeferID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Bilet seferPrFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Bilet"
    ADD CONSTRAINT "seferPrFK" FOREIGN KEY ("seferPrID") REFERENCES public."SeferProgrami"("seferProgramID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: calisanProgrami seferProgramiFK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."calisanProgrami"
    ADD CONSTRAINT "seferProgramiFK" FOREIGN KEY ("seferProgrami") REFERENCES public."SeferProgrami"("seferProgramID");


--
-- PostgreSQL database dump complete
--

