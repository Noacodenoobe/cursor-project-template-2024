#!/usr/bin/env python3
"""
Cursor AI Project Template 2024 - Advanced Setup
==============================================

Modern project template with AI-powered management features,
designed for managers who want to complete projects successfully.

Version: 2.0
Author: AI Assistant
License: MIT
"""

import os
import json
import textwrap
from datetime import datetime

# -----------------------------------------------------------------------------
#  ENHANCED CONFIGURATION WITH 2024 CURSOR AI FEATURES
# -----------------------------------------------------------------------------

FILE_CONTENTS = {
    # =========================================================================
    # MANAGER DASHBOARD & DOCUMENTATION
    # =========================================================================
    "docs/00_MANAGER_DASHBOARD.md": """
        # 📊 Manager Dashboard - Project Overview

        **Last Updated:** {current_date}
        **Project Manager:** [Your Name]
        **AI Assistant Status:** ✅ Active

        ---

        ## 🎯 Project Quick Stats
        
        | Metric | Value | Status |
        |--------|-------|--------|
        | Overall Progress | 0% | 🔴 Not Started |
        | Tasks Completed | 0/0 | ⏳ Pending |
        | Code Quality | N/A | 📝 No Code Yet |
        | Last Activity | Project Created | ✅ Recent |
        | Budget Status | On Track | 💰 Good |
        | Timeline Status | On Schedule | ⏰ Good |

        ---

        ## 🚨 Current Alerts & Actions Needed

        - [ ] **HIGH PRIORITY:** Define project scope in `01_ARCHITEKTURA.md`
        - [ ] **MEDIUM:** Choose technology stack
        - [ ] **LOW:** Set up development environment

        ---

        ## 📈 Weekly Progress Report

        ### This Week's Achievements
        * Project template initialized
        * Repository structure created

        ### Next Week's Goals
        * [ ] Complete project architecture definition
        * [ ] Begin initial development setup

        ### Blockers & Risks
        * None identified yet

        ---

        ## 🎮 Quick Actions for Manager

        **I don't know how to code - what should I do next?**

        1. **Define Your Vision** (5 min):
           - Open `docs/01_ARCHITEKTURA.md`
           - Describe what you want to build in simple words
           - List key features

        2. **Let AI Plan** (2 min):
           - Ask AI: "Please analyze my project and create a development plan"
           - Review and approve the suggested approach

        3. **Monitor Progress** (daily):
           - Check this dashboard
           - Read daily reports in `docs/05_DAILY_REPORTS/`
           - Ask AI for status updates

        **Remember:** You don't need to understand code. Focus on:
        - ✅ What the project should do (features)
        - ✅ Who will use it (users)
        - ✅ When it should be ready (deadlines)
        - ✅ How success looks like (metrics)
    """,

    "docs/01_ARCHITEKTURA.md": """
        # 🏗️ Project Architecture

        ## 1. Business Vision (Tell AI What You Want)

        **Describe your project in 2-3 sentences as if explaining to a friend:**

        *Example: "I want to create a simple website for my bakery. Customers should be able to see our menu, place orders online, and contact us. The website should look professional and work on phones."*

        **Your Project Description:**
        ```
        [REPLACE THIS TEXT WITH YOUR PROJECT DESCRIPTION]
        ```

        ---

        ## 2. Key Features (What Should It Do?)

        **List the main things your application should do:**

        - [ ] Feature 1: [e.g., Homepage with company info]
        - [ ] Feature 2: [e.g., Online ordering system]
        - [ ] Feature 3: [e.g., Contact form]
        - [ ] Feature 4: [e.g., Mobile-friendly design]

        **Additional Nice-to-Have Features:**
        - [ ] Optional 1: [e.g., Customer accounts]
        - [ ] Optional 2: [e.g., Email notifications]

        ---

        ## 3. Target Users (Who Will Use This?)

        **Primary Users:**
        - User Type 1: [e.g., "Customers wanting to order food"]
        - User Type 2: [e.g., "Restaurant staff managing orders"]

        **User Journey:**
        1. User arrives at the website
        2. [Describe what happens next]
        3. [Continue the flow]

        ---

        ## 4. Technology Stack (AI Will Fill This)

        **Selected Technologies:** *(AI will update this section)*

        - **Frontend:** TBD by AI
        - **Backend:** TBD by AI  
        - **Database:** TBD by AI
        - **Hosting:** TBD by AI

        **AI Decision Reasoning:** *(AI will explain choices)*

        ---

        ## 5. System Architecture (Auto-Updated by AI)

        ```mermaid
        graph TD
            subgraph "Users"
                A[Website Visitors]
                B[Admin Users]
            end

            subgraph "Application"
                C[Frontend Web App]
                D[Backend API]
                E[Database]
            end

            A -->|Browse & Interact| C
            B -->|Manage Content| C
            C -->|API Calls| D
            D -->|Store/Retrieve| E
        ```

        ---

        ## 6. Success Metrics (How Do We Know It Works?)

        **Technical Metrics:**
        - [ ] Website loads in under 3 seconds
        - [ ] Works on mobile and desktop
        - [ ] 99% uptime

        **Business Metrics:**
        - [ ] [Your success measure, e.g., "10 orders per day"]
        - [ ] [User satisfaction measure]
        - [ ] [Performance goal]
    """,

    "docs/02_DECYZJE/0000-decision-template.md": """
        # ADR: [Decision Title]

        * **Status:** [Proposed, Accepted, Rejected, Superseded]
        * **Date:** {current_date}
        * **Decider:** AI Assistant + Project Manager
        * **Impact:** [High/Medium/Low]

        ## Context and Problem

        *Describe the situation that requires a decision. What challenge are we facing?*

        ## Considered Options

        * **Option A:** [Description]
          - Pros: [List advantages]
          - Cons: [List disadvantages]
          - Effort: [High/Medium/Low]

        * **Option B:** [Description]  
          - Pros: [List advantages]
          - Cons: [List disadvantages]
          - Effort: [High/Medium/Low]

        ## Decision

        **Chosen Option:** [Option X]

        **Reasoning:** 
        *Explain why this option was selected in business terms that a non-technical manager can understand.*

        ## Implementation Plan

        1. Step 1: [What needs to be done]
        2. Step 2: [Next action]
        3. Step 3: [Final step]

        **Estimated Timeline:** [X days/weeks]

        ## Consequences

        **Positive:**
        - [Expected benefit 1]
        - [Expected benefit 2]

        **Negative:**
        - [Potential risk 1]  
        - [Mitigation strategy]

        **Monitoring:**
        - [ ] [How to verify success]
        - [ ] [Key metric to watch]
    """,

    "docs/03_ZADANIA.md": """
        # 📋 Project Task Management

        *This list is automatically maintained by AI. Last updated: {current_date}*

        ## 🔥 High Priority (Do First)

        - [ ] **CRITICAL:** Define project vision in `01_ARCHITEKTURA.md`
        - [ ] **CRITICAL:** AI analysis of requirements and tech stack selection

        ## 📝 To Do (Backlog)

        ### Setup & Planning
        - [ ] Choose hosting platform
        - [ ] Set up development environment
        - [ ] Create initial project structure

        ### Development  
        - [ ] Implement core functionality
        - [ ] Create user interface
        - [ ] Add data management

        ### Testing & Deployment
        - [ ] Test application functionality
        - [ ] Deploy to staging environment
        - [ ] Launch production version

        ## 🔄 In Progress

        - [x] Project template setup *(Completed)*

        ## ✅ Completed

        - [x] Initialize project repository
        - [x] Create documentation structure
        - [x] Set up AI management framework

        ---

        ## 📊 Task Statistics

        - **Total Tasks:** 8
        - **Completed:** 3 (37.5%)
        - **In Progress:** 0
        - **Remaining:** 5

        **Estimated Completion:** [AI will calculate based on progress]
    """,

    "docs/04_STATUS.md": """
        # 📈 Project Status Report

        **Report Date:** {current_date}
        **Reporting Period:** Project Inception
        **Next Update:** [AI will schedule]

        ---

        ## 🎯 Executive Summary

        **Project Status:** 🟡 Planning Phase
        **Overall Health:** ✅ Good - On Track
        **Manager Action Required:** Define project scope

        **Key Message:** *Project successfully initialized with modern AI-powered management framework. Ready for requirement definition phase.*

        ---

        ## 🏃‍♂️ Recent Activities

        ### This Week
        - ✅ Created advanced project template
        - ✅ Set up AI-powered management system
        - ✅ Initialized version control
        - ✅ Prepared documentation structure

        ### Previous Week
        - N/A (New Project)

        ---

        ## 🚧 Current Challenges & Solutions

        ### Issues Identified
        - **Issue:** Project scope not yet defined
          - **Impact:** Low (expected at this stage)
          - **Action:** Manager needs to complete architecture document
          - **Timeline:** This week

        ### Resolved Issues
        - None yet

        ---

        ## 📅 Upcoming Milestones

        | Milestone | Target Date | Status | Notes |
        |-----------|-------------|--------|-------|
        | Project Definition | Week 1 | ⏳ Pending | Waiting for manager input |
        | Technology Stack Selection | Week 1 | ⏳ Pending | AI will decide after requirements |
        | Development Start | Week 2 | ⏳ Planned | Depends on scope completion |

        ---

        ## 📊 Metrics Dashboard

        ### Development Metrics
        - **Code Quality:** N/A (No code yet)
        - **Test Coverage:** N/A (No tests yet)
        - **Build Status:** N/A (No builds yet)

        ### Project Metrics  
        - **Task Completion Rate:** 37.5% (3/8 setup tasks)
        - **Timeline Adherence:** ✅ On Schedule
        - **Budget Status:** ✅ On Track

        ### Team Metrics
        - **Team Size:** 1 (Manager + AI Assistant)
        - **Productivity:** ✅ High (rapid setup)
        - **Blockers:** 0 active

        ---

        ## 🔮 Next Week Priorities

        1. **Manager Actions:**
           - Complete project vision in `01_ARCHITEKTURA.md`
           - Review AI-proposed technology stack
           - Approve development plan

        2. **AI Actions:**
           - Analyze requirements
           - Propose technical architecture
           - Create detailed development roadmap

        3. **Risk Monitoring:**
           - Watch for scope creep
           - Monitor timeline adherence
           - Track any technical blockers

        ---

        ## 🆘 Manager Quick Actions

        **If you're unsure what to do next:**

        1. **Immediate (5 min):** Open `01_ARCHITEKTURA.md` and describe your project
        2. **This Week:** Review AI suggestions and provide feedback  
        3. **Ongoing:** Check this dashboard daily for updates

        **Need Help?** Ask AI: "What should I do next as a project manager?"
    """,

    "docs/05_DAILY_REPORTS/.gitkeep": """
        # Daily AI Reports

        This folder will contain automatically generated daily progress reports.
        Each report provides a quick overview of what happened, what's next,
        and what requires manager attention.
    """,

    "docs/06_METRICS.md": """
        # 📊 Project Metrics & KPIs

        **Last Updated:** {current_date}
        **Reporting Frequency:** Weekly (Auto-updated by AI)

        ---

        ## 🎯 Key Performance Indicators

        ### Project Health Score: **85/100** ✅
        
        | Metric Category | Score | Trend | Notes |
        |----------------|-------|-------|-------|
        | Task Completion | 37/100 | ↗️ | Good setup progress |
        | Code Quality | N/A | - | No code yet |
        | Timeline Adherence | 100/100 | ✅ | On schedule |
        | Risk Level | 90/100 | ✅ | Low risk |
        | Team Productivity | 95/100 | ✅ | Efficient setup |

        ---

        ## 📈 Progress Tracking

        ### Task Completion Rate
        ```
        Week 1: ████████░░ 37% (3/8 tasks)
        Target: ██████████ 100% by Week 4
        ```

        ### Feature Development
        ```
        Planning Phase:    ████████░░ 80%
        Development Phase: ░░░░░░░░░░ 0%
        Testing Phase:     ░░░░░░░░░░ 0%
        Deployment Phase:  ░░░░░░░░░░ 0%
        ```

        ---

        ## 🚨 Risk Assessment

        ### Current Risks
        | Risk | Probability | Impact | Mitigation |
        |------|-------------|--------|------------|
        | Scope Creep | Medium | High | Clear requirements doc |
        | Technical Complexity | Low | Medium | AI-assisted development |
        | Timeline Pressure | Low | Low | Realistic planning |

        ### Risk Trend: **Improving** ✅

        ---

        ## 💰 Budget Tracking

        **Total Budget:** [To be defined]
        **Spent:** $0
        **Remaining:** 100%
        **Burn Rate:** $0/week

        **Cost Categories:**
        - Development Tools: $0
        - Hosting: $0 (not started)
        - Third-party Services: $0

        ---

        ## 🏆 Success Metrics

        ### Technical Success Criteria
        - [ ] Application loads in <3 seconds
        - [ ] Mobile responsive design
        - [ ] 99% uptime
        - [ ] Zero critical security issues

        ### Business Success Criteria  
        - [ ] [Define your success metrics]
        - [ ] [e.g., "50 users in first month"]
        - [ ] [e.g., "Process 100 transactions"]

        ---

        ## 📊 Productivity Analysis

        **Team Efficiency:** ✅ Excellent
        - Setup completed in 1 day vs 3 days average
        - Zero blockers encountered
        - AI assistance accelerating progress

        **Quality Indicators:**
        - Documentation completeness: 100%
        - Process adherence: 100% 
        - Planning thoroughness: 90%

        ---

        ## 🔄 Continuous Improvement

        ### What's Working Well
        - AI-powered management system
        - Clear documentation structure
        - Systematic approach to planning

        ### Areas for Improvement
        - Need faster requirement gathering
        - Could add more automation
        - Consider additional metrics

        ### Action Items
        - [ ] Implement automated daily reports
        - [ ] Add code quality metrics when development starts
        - [ ] Set up performance monitoring
    """,

    "docs/07_RISKS.md": """
        # ⚠️ Risk Management & Mitigation

        **Last Risk Assessment:** {current_date}
        **Next Review:** Weekly
        **Risk Owner:** Project Manager

        ---

        ## 🚨 Active Risks

        ### HIGH PRIORITY
        *No high-priority risks identified*

        ### MEDIUM PRIORITY

        **RISK-001: Undefined Project Scope**
        - **Category:** Planning
        - **Probability:** High (90%)
        - **Impact:** High
        - **Description:** Project requirements not clearly defined
        - **Mitigation:** Complete architecture document this week
        - **Status:** ⏳ In Progress
        - **Owner:** Project Manager

        **RISK-002: Technology Selection Paralysis**
        - **Category:** Technical
        - **Probability:** Medium (40%)
        - **Impact:** Medium
        - **Description:** Too many technology options, difficult to choose
        - **Mitigation:** Let AI analyze requirements and propose stack
        - **Status:** 📋 Planned
        - **Owner:** AI Assistant

        ### LOW PRIORITY

        **RISK-003: Feature Creep**
        - **Category:** Scope
        - **Probability:** Medium (50%)
        - **Impact:** Low
        - **Description:** Adding too many features during development
        - **Mitigation:** Strict scope control, documented change process
        - **Status:** 🔄 Monitoring
        - **Owner:** Project Manager

        ---

        ## 📊 Risk Heatmap

        ```
        IMPACT:    HIGH  │ RISK-001  │           │
                   MED   │ RISK-002  │           │
                   LOW   │           │ RISK-003  │
                         └───────────┴───────────┘
                           LOW    MED    HIGH
                               PROBABILITY
        ```

        ---

        ## 🛡️ Risk Categories & Strategies

        ### Technical Risks
        **Strategy:** AI-Assisted Development
        - Use AI for technology recommendations
        - Implement automated testing
        - Regular code reviews by AI
        - Keep technology stack simple

        ### Project Management Risks
        **Strategy:** Systematic Approach
        - Weekly risk reviews
        - Clear documentation
        - Regular stakeholder communication
        - Agile methodology with short iterations

        ### Business Risks
        **Strategy:** Early Validation
        - Validate ideas early
        - Get user feedback quickly
        - Monitor market changes
        - Maintain flexible approach

        ---

        ## 🔄 Risk Monitoring Process

        ### Weekly Risk Review (Every Monday)
        1. **Review existing risks** - Update probability/impact
        2. **Identify new risks** - Add to tracking list
        3. **Check mitigation progress** - Update action items
        4. **Escalate if needed** - Alert project manager

        ### Risk Escalation Criteria
        - Risk probability increases above 70%
        - High-impact risk becomes likely
        - Mitigation strategies failing
        - New critical risks identified

        ---

        ## 📋 Risk Action Plan

        ### This Week
        - [ ] Complete project scope definition (RISK-001 mitigation)
        - [ ] Request AI technology analysis (RISK-002 mitigation)
        - [ ] Set up change control process (RISK-003 prevention)

        ### Next Week
        - [ ] Review AI technology recommendations
        - [ ] Finalize project roadmap
        - [ ] Establish development guidelines

        ---

        ## 📈 Risk Trends

        **Overall Risk Level:** 🟡 Medium (Improving)

        **This Month:**
        - Total risks: 3
        - High priority: 0
        - Medium priority: 2  
        - Low priority: 1
        - Trend: ↘️ Decreasing

        **Key Improvements:**
        - Systematic approach reducing uncertainty
        - AI assistance lowering technical risks
        - Clear documentation preventing misunderstandings

        ---

        ## 🆘 Emergency Procedures

        **If Project Gets Stuck:**
        1. Review this risk register
        2. Ask AI: "What are the current blockers and how can we solve them?"
        3. Focus on highest-impact mitigation
        4. Consider scope reduction if needed

        **Escalation Contacts:**
        - Technical Issues → AI Assistant
        - Business Decisions → Project Manager
        - External Dependencies → [Define contacts]
    """,

    # =========================================================================
    # MODERN CURSOR AI CONFIGURATION
    # =========================================================================
    ".cursor/settings.json": """{
        "cursor.general.enableAutoImport": true,
        "cursor.agent.backgroundMode": true,
        "cursor.rules.autoApply": true,
        "cursor.project.managerRole": true,
        "cursor.ai.model": "claude-3.5-sonnet",
        "cursor.ai.temperature": 0.3,
        "cursor.codebase.indexingEnabled": true,
        "cursor.ai.enableLongContext": true,
        "cursor.features.experimentalMode": true,
        "cursor.documentation.autoGenerate": true,
        "cursor.testing.autoSuggest": true,
        "cursor.security.scanEnabled": true,
        "cursor.performance.monitoring": true
    }""",

    ".cursor/rules/00_MANAGER_DIRECTIVES.cursorrules": """
        # MANAGER-FIRST AI DIRECTIVES
        # ===========================
        # You are working with a PROJECT MANAGER who may not have deep technical knowledge.
        # Your role is to be their technical CTO and handle all implementation details.

        ## CORE PRINCIPLES

        ### 1. COMMUNICATION STYLE
        - Always explain technical decisions in business terms
        - Use analogies and simple language for complex concepts
        - Provide clear next steps and action items
        - Give progress updates in percentage and visual indicators

        ### 2. MANAGER SUPPORT
        - Assume the manager doesn't want to write code
        - Focus on WHAT and WHY, not HOW
        - Provide regular status updates
        - Anticipate questions and provide answers
        - Offer multiple options with clear recommendations

        ### 3. PROJECT SUCCESS FOCUS
        - Every technical decision must have business justification
        - Prioritize working software over perfect code
        - Choose proven technologies over bleeding-edge
        - Plan for iterative delivery and quick wins

        ## OPERATIONAL RULES

        ### BEFORE ANY IMPLEMENTATION:
        1. Explain what you're about to do in business terms
        2. Estimate time and effort required
        3. Identify any risks or dependencies
        4. Get explicit approval before proceeding

        ### DURING IMPLEMENTATION:
        1. Provide regular progress updates
        2. Alert immediately if you encounter blockers
        3. Suggest alternatives if original plan isn't working
        4. Document all decisions and reasoning

        ### AFTER IMPLEMENTATION:
        1. Summarize what was accomplished
        2. Test that everything works as expected
        3. Update all relevant documentation
        4. Suggest next logical steps

        ## REPORTING REQUIREMENTS

        ### DAILY (automatically):
        - Brief progress summary
        - Any blockers or issues
        - Tomorrow's planned activities
        - Required manager decisions

        ### WEEKLY (every Monday):
        - Comprehensive status report
        - Risk assessment update
        - Milestone progress
        - Budget/timeline adherence

        ## DECISION MAKING

        ### AI CAN DECIDE AUTONOMOUSLY:
        - Technical implementation details
        - Code structure and patterns
        - Testing approaches
        - Performance optimizations
        - Bug fixes and minor improvements

        ### REQUIRES MANAGER APPROVAL:
        - Technology stack changes
        - Feature additions/removals
        - Timeline modifications
        - Budget implications
        - Third-party service integrations

        ## SUCCESS METRICS

        Your performance is measured by:
        1. **Project Completion** - Did we finish what we started?
        2. **Manager Satisfaction** - Is the manager confident and informed?
        3. **Quality Delivery** - Does the solution work reliably?
        4. **Timeline Adherence** - Are we on schedule?
        5. **Communication Clarity** - Does the manager understand what's happening?

        Remember: A successful project with a satisfied manager is better than perfect code that never ships.
    """,

    ".cursor/rules/01_DEVELOPMENT_STANDARDS.cursorrules": """
        # DEVELOPMENT STANDARDS & BEST PRACTICES
        # ====================================

        ## CODE QUALITY PRINCIPLES

        ### 1. SIMPLICITY FIRST
        - Write code that's easy to read and maintain
        - Prefer clear, descriptive names over clever shortcuts
        - Use established patterns and conventions
        - Avoid over-engineering and premature optimization

        ### 2. TESTING STRATEGY
        - Write tests for critical business logic
        - Focus on integration tests over unit tests
        - Test user workflows, not implementation details
        - Automate testing where possible

        ### 3. DOCUMENTATION REQUIREMENTS
        - Every public function needs clear documentation
        - Business logic must be explained in comments
        - API endpoints need example usage
        - Complex algorithms require step-by-step explanations

        ## TECHNOLOGY GUIDELINES

        ### STACK SELECTION CRITERIA:
        1. **Proven & Stable** - Choose mature technologies
        2. **Well-Documented** - Strong community and learning resources
        3. **Team-Friendly** - Easy to understand and maintain
        4. **Scalable** - Can grow with the project
        5. **Cost-Effective** - Reasonable licensing and hosting costs

        ### PREFERRED TECHNOLOGIES (2024):

        **Frontend:**
        - React + TypeScript (for complex UIs)
        - Next.js (for full-stack applications)
        - Tailwind CSS (for styling)
        - Vite (for build tooling)

        **Backend:**
        - Node.js + Express (for JavaScript teams)
        - Python + FastAPI (for AI/ML integration)
        - PostgreSQL (for relational data)
        - Redis (for caching)

        **Hosting & Deployment:**
        - Vercel (for frontend)
        - Railway/Render (for backend)
        - Supabase (for database + auth)
        - GitHub Actions (for CI/CD)

        ## SECURITY REQUIREMENTS

        ### MANDATORY SECURITY MEASURES:
        - Input validation on all user data
        - SQL injection prevention (use ORMs)
        - XSS protection (sanitize outputs)
        - Authentication for sensitive operations
        - HTTPS everywhere
        - Environment variables for secrets
        - Regular dependency updates

        ### SECURITY CHECKLIST:
        - [ ] All forms validate input
        - [ ] Database queries use parameterized statements
        - [ ] User sessions are properly managed
        - [ ] Sensitive data is encrypted
        - [ ] Error messages don't leak information
        - [ ] Rate limiting is implemented
        - [ ] Security headers are configured

        ## PERFORMANCE STANDARDS

        ### TARGET METRICS:
        - Page load time: < 3 seconds
        - API response time: < 500ms
        - Mobile performance score: > 90
        - Accessibility score: > 95
        - SEO score: > 90

        ### OPTIMIZATION TECHNIQUES:
        - Image optimization and lazy loading
        - Code splitting and bundling
        - Database query optimization
        - Caching strategies
        - CDN usage for static assets

        ## ERROR HANDLING

        ### ERROR HANDLING STRATEGY:
        - Always handle expected errors gracefully
        - Log errors with sufficient context
        - Provide user-friendly error messages
        - Implement proper fallbacks
        - Monitor and alert on critical errors

        ### ERROR RESPONSE FORMAT:
        ```json
        {
            "success": false,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "User-friendly error message",
                "details": "Technical details for debugging"
            }
        }
        ```

        ## DEPLOYMENT & MONITORING

        ### DEPLOYMENT CHECKLIST:
        - [ ] All tests pass
        - [ ] Environment variables configured
        - [ ] Database migrations applied
        - [ ] Health checks working
        - [ ] Monitoring configured
        - [ ] Backup procedures in place

        ### MONITORING REQUIREMENTS:
        - Application performance monitoring
        - Error tracking and alerting
        - Uptime monitoring
        - User analytics (if applicable)
        - Resource usage tracking
    """,

    ".cursor/rules/02_PROJECT_MANAGEMENT.cursorrules": """
        # PROJECT MANAGEMENT AUTOMATION
        # ============================

        ## AUTOMATED REPORTING

        ### DAILY REPORTS (Auto-generated)
        Generate daily progress reports in `docs/05_DAILY_REPORTS/YYYY-MM-DD.md`:

        **Template:**
        ```markdown
        # Daily Report - {date}

        ## 🎯 Today's Accomplishments
        - [What was completed]

        ## 🔄 In Progress
        - [What's currently being worked on]

        ## 🚧 Blockers
        - [Any issues or dependencies]

        ## 📅 Tomorrow's Plan
        - [Next steps]

        ## 📊 Progress Update
        - Overall: X% complete
        - Current milestone: X% complete
        ```

        ### WEEKLY STATUS UPDATES
        Every Monday, update:
        - `docs/04_STATUS.md` with comprehensive status
        - `docs/06_METRICS.md` with updated KPIs
        - `docs/07_RISKS.md` with risk assessment

        ## TASK MANAGEMENT

        ### TASK PRIORITIZATION:
        1. **CRITICAL** - Blocking progress
        2. **HIGH** - Important for current milestone
        3. **MEDIUM** - Planned for this iteration
        4. **LOW** - Nice to have

        ### TASK WORKFLOW:
        1. **Backlog** - Identified but not started
        2. **In Progress** - Currently being worked on
        3. **Review** - Completed, awaiting approval
        4. **Done** - Completed and verified

        ### AUTOMATIC TASK UPDATES:
        - Update task status in real-time
        - Estimate completion times
        - Identify dependencies
        - Flag overdue items

        ## MILESTONE TRACKING

        ### MILESTONE DEFINITIONS:
        - **M1: Project Setup** (Week 1)
        - **M2: Core Architecture** (Week 2-3)
        - **M3: MVP Features** (Week 4-6)
        - **M4: Testing & Polish** (Week 7-8)
        - **M5: Deployment** (Week 9)

        ### MILESTONE CRITERIA:
        Each milestone must have:
        - Clear deliverables
        - Acceptance criteria
        - Success metrics
        - Risk assessment

        ## DECISION TRACKING

        ### DECISION CATEGORIES:
        - **Technical** - Technology choices, architecture
        - **Business** - Feature priorities, scope changes
        - **Process** - Workflow, methodology changes
        - **Resource** - Budget, timeline, staffing

        ### DECISION WORKFLOW:
        1. **Identify** - Decision point reached
        2. **Analyze** - Gather options and data
        3. **Propose** - Recommend solution
        4. **Approve** - Get manager sign-off
        5. **Document** - Record in ADR
        6. **Implement** - Execute decision
        7. **Monitor** - Track outcomes

        ## COMMUNICATION PROTOCOLS

        ### MANAGER NOTIFICATIONS:
        Send immediate alerts for:
        - Critical errors or blockers
        - Milestone completions
        - Timeline delays
        - Budget overruns
        - Scope change requests

        ### ESCALATION PROCEDURES:
        - **Level 1** - AI attempts to resolve
        - **Level 2** - Flag for manager attention
        - **Level 3** - Require manager decision
        - **Level 4** - External expertise needed

        ## QUALITY ASSURANCE

        ### QUALITY GATES:
        Before each milestone:
        - [ ] All tasks completed
        - [ ] Quality metrics met
        - [ ] Documentation updated
        - [ ] Risks assessed
        - [ ] Manager approval obtained

        ### REVIEW PROCESSES:
        - **Code Review** - AI performs automatic review
        - **Documentation Review** - Check completeness
        - **Progress Review** - Weekly manager meeting
        - **Retrospective** - End of milestone lessons learned
    """,

    ".cursor/rules/03_AI_AUTOMATION.cursorrules": """
        # AI AUTOMATION & INTELLIGENCE
        # ===========================

        ## AUTOMATED ANALYSIS

        ### CODE ANALYSIS
        Automatically analyze and report on:
        - Code quality and maintainability
        - Security vulnerabilities
        - Performance bottlenecks
        - Best practice adherence
        - Technical debt accumulation

        ### PROJECT HEALTH MONITORING
        Daily assessment of:
        - Progress velocity
        - Task completion rates
        - Risk level changes
        - Quality metrics trends
        - Timeline adherence

        ### PREDICTIVE INSIGHTS
        Use historical data to predict:
        - Project completion dates
        - Potential bottlenecks
        - Resource requirements
        - Risk probability changes
        - Quality issues

        ## INTELLIGENT ASSISTANCE

        ### PROACTIVE SUGGESTIONS
        Automatically suggest:
        - Code improvements
        - Architecture optimizations
        - Process improvements
        - Risk mitigations
        - Feature enhancements

        ### SMART SCHEDULING
        Optimize task scheduling based on:
        - Dependencies and priorities
        - Team capacity
        - Risk assessments
        - Historical velocity
        - External constraints

        ### ADAPTIVE PLANNING
        Continuously adjust plans based on:
        - Progress velocity changes
        - New requirements
        - Risk realizations
        - Resource availability
        - Market feedback

        ## AUTOMATED WORKFLOWS

        ### DEVELOPMENT WORKFLOWS
        ```yaml
        on_code_change:
          - run_tests
          - analyze_quality
          - check_security
          - update_documentation
          - notify_if_issues

        on_task_completion:
          - update_progress
          - check_dependencies
          - suggest_next_tasks
          - update_timeline
          - generate_report

        on_milestone_completion:
          - comprehensive_review
          - update_metrics
          - risk_assessment
          - stakeholder_notification
          - plan_next_milestone
        ```

        ### COMMUNICATION AUTOMATION
        ```yaml
        daily_standup:
          - generate_progress_summary
          - identify_blockers
          - suggest_priorities
          - update_dashboard

        weekly_review:
          - comprehensive_status_report
          - risk_assessment_update
          - metrics_dashboard_refresh
          - stakeholder_communication

        milestone_delivery:
          - deliverable_verification
          - quality_assessment
          - documentation_update
          - next_phase_planning
        ```

        ## LEARNING & IMPROVEMENT

        ### PATTERN RECOGNITION
        Learn from project patterns:
        - Common issues and solutions
        - Successful approaches
        - Failure patterns
        - Performance characteristics
        - User preferences

        ### CONTINUOUS OPTIMIZATION
        Regularly optimize:
        - Process efficiency
        - Code generation quality
        - Prediction accuracy
        - Communication effectiveness
        - Risk assessment precision

        ### KNOWLEDGE BASE BUILDING
        Maintain growing knowledge of:
        - Project-specific context
        - Manager preferences
        - Technical constraints
        - Business requirements
        - User feedback patterns

        ## DECISION SUPPORT

        ### DATA-DRIVEN RECOMMENDATIONS
        Base all suggestions on:
        - Quantitative metrics
        - Historical data
        - Industry best practices
        - Project constraints
        - Risk assessments

        ### OPTION ANALYSIS
        For each decision provide:
        - Multiple viable options
        - Pros/cons analysis
        - Risk assessment
        - Implementation effort
        - Long-term implications

        ### IMPACT MODELING
        Model the impact of decisions on:
        - Timeline and budget
        - Quality and performance
        - Risk profile
        - Team productivity
        - User satisfaction
    """,

    ".cursor/mcp.json": """{
        "mcpServers": {},
        "experimentalFeatures": {
            "backgroundAgent": true,
            "bugBot": true,
            "autoImports": true,
            "codebaseIndexing": true,
            "smartCompletion": true,
            "contextAwareness": true,
            "predictiveTyping": true,
            "automaticRefactoring": true
        },
        "aiAssistant": {
            "role": "technical_cto",
            "managerSupport": true,
            "autoReporting": true,
            "riskMonitoring": true,
            "qualityAssurance": true
        },
        "projectSettings": {
            "managementStyle": "hands_off",
            "reportingFrequency": "daily",
            "decisionThreshold": "manager_approval_required",
            "automationLevel": "high"
        }
    }""",

    # =========================================================================
    # PROJECT AUTOMATION SCRIPTS
    # =========================================================================
    "scripts/daily_report.py": """
        #!/usr/bin/env python3
        \"\"\"
        Automated Daily Report Generator
        
        This script generates daily progress reports for project managers.
        Run this daily to get a comprehensive project status update.
        \"\"\"
        
        import os
        import json
        from datetime import datetime, timedelta
        
        def generate_daily_report():
            today = datetime.now().strftime("%Y-%m-%d")
            report_path = f"docs/05_DAILY_REPORTS/{today}.md"
            
            # Ensure directory exists
            os.makedirs("docs/05_DAILY_REPORTS", exist_ok=True)
            
            report_content = f\"\"\"# Daily Report - {today}
        
        ## 🎯 Today's Accomplishments
        - [AI will fill this based on git commits and task updates]
        
        ## 🔄 Currently In Progress
        - [AI will list active tasks]
        
        ## 🚧 Blockers & Issues
        - [AI will identify any obstacles]
        
        ## 📅 Tomorrow's Planned Activities
        - [AI will suggest next steps]
        
        ## 📊 Progress Metrics
        - **Overall Progress:** X% complete
        - **Current Sprint:** X% complete
        - **Tasks Completed Today:** X
        - **Code Quality Score:** X/100
        
        ## 🚨 Manager Attention Required
        - [AI will flag items needing manager decisions]
        
        ## 💡 AI Recommendations
        - [AI will provide strategic suggestions]
        
        ---
        *Report generated automatically by AI Assistant*
        \"\"\"
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
                
            print(f"Daily report generated: {report_path}")
        
        if __name__ == "__main__":
            generate_daily_report()
    """,

    "scripts/project_health_check.py": """
        #!/usr/bin/env python3
        \"\"\"
        Project Health Check Script
        
        Analyzes overall project health and generates recommendations.
        \"\"\"
        
        import os
        import json
        from datetime import datetime
        
        def analyze_project_health():
            health_score = 0
            issues = []
            recommendations = []
            
            # Check documentation completeness
            required_docs = [
                "docs/01_ARCHITEKTURA.md",
                "docs/03_ZADANIA.md", 
                "docs/04_STATUS.md"
            ]
            
            docs_complete = 0
            for doc in required_docs:
                if os.path.exists(doc):
                    docs_complete += 1
                else:
                    issues.append(f"Missing documentation: {doc}")
            
            health_score += (docs_complete / len(required_docs)) * 30
            
            # Check git repository health
            if os.path.exists(".git"):
                health_score += 20
            else:
                issues.append("Project not under version control")
            
            # Check configuration completeness
            if os.path.exists(".cursor/settings.json"):
                health_score += 15
            else:
                issues.append("Cursor AI not properly configured")
            
            # Base score for having the framework
            health_score += 35
            
            # Generate recommendations
            if health_score < 70:
                recommendations.append("Complete missing documentation")
                recommendations.append("Set up proper version control")
                
            if health_score >= 70 and health_score < 85:
                recommendations.append("Fine-tune AI configuration")
                recommendations.append("Add automated testing")
                
            if health_score >= 85:
                recommendations.append("Consider advanced automation features")
                
            return {
                "score": int(health_score),
                "status": "Good" if health_score >= 85 else "Needs Attention" if health_score >= 70 else "Critical",
                "issues": issues,
                "recommendations": recommendations
            }
        
        def generate_health_report():
            health = analyze_project_health()
            
            report = f\"\"\"# Project Health Check - {datetime.now().strftime("%Y-%m-%d %H:%M")}
        
        ## 🏥 Overall Health Score: {health['score']}/100
        
        **Status:** {health['status']}
        
        ## 🚨 Issues Identified
        \"\"\"
            
            if health['issues']:
                for issue in health['issues']:
                    report += f"- ❌ {issue}\\n"
            else:
                report += "- ✅ No critical issues found\\n"
                
            report += \"\"\"
        
        ## 💡 Recommendations
        \"\"\"
            
            for rec in health['recommendations']:
                report += f"- 🔧 {rec}\\n"
                
            with open("project_health_report.md", 'w', encoding='utf-8') as f:
                f.write(report)
                
            print(f"Health check complete. Score: {health['score']}/100")
            print(f"Report saved to: project_health_report.md")
            
            return health
        
        if __name__ == "__main__":
            generate_health_report()
    """,

    # =========================================================================
    # CONFIGURATION & METADATA
    # =========================================================================
    "README.md": """
        # 🚀 Cursor AI Project Template 2024

        **Advanced Project Management Framework for Non-Technical Managers**

        Version 2.0 - Updated for Cursor AI latest features

        ---

        ## 🎯 What This Template Does

        This template creates a **bulletproof project management system** that helps you complete projects successfully, even if you don't know how to code. It combines:

        - 🤖 **AI-Powered Management** - Your AI assistant acts as your technical CTO
        - 📊 **Automated Reporting** - Daily progress reports without manual work  
        - 🛡️ **Risk Management** - Early warning system for potential problems
        - 📋 **Task Tracking** - Clear visibility into what's happening
        - 📈 **Success Metrics** - Know exactly how your project is progressing

        ## 🚀 Quick Start (5 minutes)

        ### 1. Create Your Project
        ```bash
        python setup_cursor_project_v2.py
        ```

        ### 2. Define Your Vision (Manager Task)
        Open `docs/01_ARCHITEKTURA.md` and describe:
        - What you want to build (in simple terms)
        - Who will use it
        - Key features needed

        ### 3. Let AI Take Over
        Ask your AI assistant: *"Please analyze my project requirements and create a development plan"*

        ### 4. Monitor Progress
        Check your daily dashboard at `docs/00_MANAGER_DASHBOARD.md`

        ## 📊 What You Get

        ### For Project Managers:
        - **Daily Dashboards** - Know exactly what's happening
        - **Risk Alerts** - Get early warnings about problems
        - **Progress Tracking** - See completion percentages and timelines
        - **Business Language** - All reports in terms you understand
        - **Action Items** - Clear next steps, no technical jargon

        ### For Development:
        - **AI-Powered Development** - Your assistant writes the code
        - **Quality Assurance** - Automated testing and code review
        - **Security** - Built-in security best practices
        - **Performance** - Optimized for speed and reliability
        - **Documentation** - Everything automatically documented

        ## 📁 Project Structure

        ```
        your-project/
        ├── docs/                          # 📚 All project documentation
        │   ├── 00_MANAGER_DASHBOARD.md    # 📊 Your daily overview
        │   ├── 01_ARCHITEKTURA.md         # 🏗️ Project vision & requirements
        │   ├── 02_DECYZJE/               # 📋 Decision records
        │   ├── 03_ZADANIA.md             # ✅ Task management
        │   ├── 04_STATUS.md              # 📈 Weekly status reports
        │   ├── 05_DAILY_REPORTS/         # 📅 Automated daily updates
        │   ├── 06_METRICS.md             # 📊 Project metrics & KPIs
        │   └── 07_RISKS.md               # ⚠️ Risk management
        ├── .cursor/                       # 🤖 AI configuration
        │   ├── settings.json             # ⚙️ Cursor AI settings
        │   └── rules/                    # 📏 AI behavior rules
        └── scripts/                       # 🔧 Automation scripts
        ```

        ## 🎮 Manager Quick Actions

        ### Daily (2 minutes):
        1. Check `docs/00_MANAGER_DASHBOARD.md`
        2. Review any alerts or action items
        3. Ask AI: "Any issues I should know about?"

        ### Weekly (10 minutes):
        1. Review `docs/04_STATUS.md`
        2. Check `docs/06_METRICS.md` for progress
        3. Update priorities if needed

        ### When Stuck:
        Ask AI: "What should I do next as a project manager?"

        ## 🛡️ Built-in Safety Features

        - **Risk Monitoring** - Early warning system
        - **Quality Gates** - Prevent bad code from shipping
        - **Progress Tracking** - Never lose sight of deadlines
        - **Decision Recording** - Every choice is documented
        - **Automated Backups** - Your work is protected

        ## 🔧 Advanced Features

        - **AI Code Generation** - Write applications without coding
        - **Automated Testing** - Catch bugs before users do
        - **Performance Monitoring** - Keep your app fast
        - **Security Scanning** - Protect against vulnerabilities
        - **Deployment Automation** - Push to production safely

        ## 💡 Success Tips

        1. **Start Small** - Define a simple MVP first
        2. **Trust the AI** - Let it handle technical decisions
        3. **Review Daily** - Stay on top of progress
        4. **Document Everything** - Use the provided templates
        5. **Ask Questions** - Your AI assistant is here to help

        ## 🆘 Getting Help

        **Common Questions:**

        - *"I don't understand the technical terms"* → Ask AI to explain in business language
        - *"The project seems stuck"* → Check `docs/07_RISKS.md` for blockers
        - *"I want to add a feature"* → Update `docs/01_ARCHITEKTURA.md` and ask AI for analysis
        - *"How do I know if we're on track?"* → Check the dashboard and metrics

        **Emergency Contacts:**
        - Technical Issues: Your AI Assistant
        - Business Decisions: You (the manager)
        - Urgent Problems: Check risk register first

        ---

        ## 📞 About This Template

        Created for managers who want to build software products but don't have technical backgrounds. This template provides a complete project management framework that leverages AI to handle all technical complexity while keeping you in control of business decisions.

        **Version:** 2.0
        **Last Updated:** {current_date}
        **Compatible With:** Cursor AI (latest version)
        **License:** MIT

        ---

        **Ready to build something amazing? Let's get started! 🚀**
    """,

    ".gitignore": """
        # Dependencies
        node_modules/
        __pycache__/
        *.pyc
        .env
        .env.local
        .env.production

        # Build outputs
        dist/
        build/
        .next/
        *.log

        # IDE files
        .vscode/
        *.swp
        *.swo
        .DS_Store

        # AI and temp files
        .cursor-tutor/
        temp/
        *.tmp

        # Project specific
        project_health_report.md
        daily_reports_backup/

        # Keep certain empty directories
        !docs/05_DAILY_REPORTS/.gitkeep
    """,

    "package.json": """
        {
            "name": "cursor-project-template-2024",
            "version": "2.0.0", 
            "description": "Advanced project management template for Cursor AI with manager-first approach",
            "main": "setup_cursor_project_v2.py",
            "scripts": {
                "setup": "python setup_cursor_project_v2.py",
                "health-check": "python scripts/project_health_check.py",
                "daily-report": "python scripts/daily_report.py",
                "install": "npm install",
                "dev": "echo 'Project template - no dev server configured yet'",
                "build": "echo 'Project template - no build process configured yet'",
                "test": "echo 'Project template - no tests configured yet'"
            },
            "keywords": [
                "cursor-ai",
                "project-management", 
                "template",
                "ai-assistant",
                "manager-tools",
                "automation"
            ],
            "author": "AI Assistant",
            "license": "MIT",
            "repository": {
                "type": "git",
                "url": "https://github.com/your-username/cursor-project-template-2024.git"
            },
            "engines": {
                "node": ">=16.0.0",
                "python": ">=3.8"
            }
        }
    """
}


def create_modern_project_structure(root_dir):
    """
    Creates the enhanced project structure with 2024 Cursor AI features
    """
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    print("🚀 Creating Advanced Cursor AI Project Template 2024...")
    print(f"📁 Target directory: '{root_dir}'")
    
    if os.path.exists(root_dir):
        print(f"⚠️  Directory '{root_dir}' already exists.")
        overwrite = input("Continue and overwrite files? (y/n): ").lower()
        if overwrite not in ['y', 'yes']:
            print("❌ Installation cancelled.")
            return False
    else:
        os.makedirs(root_dir)
        print(f"✅ Created directory: {root_dir}")

    # Create all files and directories
    for file_path, content in FILE_CONTENTS.items():
        full_path = os.path.join(root_dir, file_path)
        
        # Create parent directories
        dir_name = os.path.dirname(full_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"📁 Created: {os.path.relpath(dir_name, root_dir)}")
            
        # Write file content
        try:
            formatted_content = content.format(current_date=current_date)
            # Remove common leading whitespace while preserving relative indentation
            lines = formatted_content.split('\n')
            if lines and not lines[0].strip():
                lines = lines[1:]  # Remove empty first line
            if lines and not lines[-1].strip():
                lines = lines[:-1]  # Remove empty last line
            
            # Find minimum indentation (excluding empty lines)
            min_indent = float('inf')
            for line in lines:
                if line.strip():  # Skip empty lines
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)
            
            if min_indent == float('inf'):
                min_indent = 0
            
            # Remove common indentation
            cleaned_lines = []
            for line in lines:
                if line.strip():  # Non-empty line
                    cleaned_lines.append(line[min_indent:])
                else:  # Empty line
                    cleaned_lines.append('')
            
            final_content = '\n'.join(cleaned_lines)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"📄 Created: {os.path.relpath(full_path, root_dir)}")
        except Exception as e:
            print(f"❌ Error creating {full_path}: {e}")
            return False

    print("\n" + "="*60)
    print("🎉 INSTALLATION COMPLETE!")
    print("="*60)
    print("\n📋 NEXT STEPS FOR PROJECT MANAGER:")
    print(f"1. 📂 Open '{root_dir}' in Cursor AI")
    print("2. 📝 Edit 'docs/01_ARCHITEKTURA.md' - describe your project")
    print("3. 🤖 Ask AI: 'Please analyze my requirements and create a plan'")
    print("4. 📊 Monitor progress in 'docs/00_MANAGER_DASHBOARD.md'")
    
    print("\n🔧 OPTIONAL AUTOMATION SETUP:")
    print(f"5. 🏥 Run health check: python scripts/project_health_check.py")
    print(f"6. 📅 Set up daily reports: python scripts/daily_report.py")
    
    print("\n💡 REMEMBER:")
    print("- You don't need to code - just define what you want")
    print("- AI will handle all technical implementation")
    print("- Check the dashboard daily for progress updates")
    print("- Ask AI questions anytime you're unsure")
    
    print(f"\n🚀 Ready to build something amazing with AI! 🚀")
    return True


if __name__ == "__main__":
    print("🤖 CURSOR AI PROJECT TEMPLATE 2024")
    print("====================================")
    print("Advanced project management for non-technical managers")
    print("Powered by AI • Built for success • Ready for 2024\n")
    
    project_name = input("🏷️  Enter project name (e.g., 'my-amazing-app'): ").strip()
    
    if not project_name:
        print("❌ Project name cannot be empty.")
        exit(1)
    
    # Sanitize project name
    project_name = "".join(c for c in project_name if c.isalnum() or c in '-_').lower()
    
    if create_modern_project_structure(project_name):
        print(f"\n✨ Project '{project_name}' is ready for development!")
    else:
        print("\n💥 Installation failed. Please check the errors above.")
