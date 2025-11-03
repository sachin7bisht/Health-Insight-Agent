create table users (
 id uuid primary key default gen_random_uuid(),
 email text not null unique,
name text,
created_at timestamptz default now()
);


create table chat_sessions (
id uuid primary key default gen_random_uuid(),
user_id UUID NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id),
-- user_id FOREIGN KEY references users(id),
title text,
created_at timestamptz default now()
);

create table chat_messages(
id uuid primary key default gen_random_uuid(),
session_id UUID NOT NULL,
FOREIGN KEY (session_id) REFERENCES chat_sessions(id),
-- session_id uuid foreign key not null references chat_session(id),
content text,
role text,
created_at timestamptz default now()
);

CREATE INDEX idx_chat_sessions_user_id ON chat_sessions(user_id);
CREATE INDEX idx_chat_messages_session_id ON chat_messages(session_id);

CREATE TABLE analyses (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid, -- from supabase auth
  uploaded_at timestamptz DEFAULT now(),
  file_name text,
  raw_text text,
  summary text,
  flags jsonb,
  llm_response jsonb,
  created_at timestamptz DEFAULT now()
);

CREATE INDEX ON analyses (user_id);