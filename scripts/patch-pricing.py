#!/usr/bin/env python3
"""
Patch the pre-rendered pricing section in index.html with the new 3-tier pricing,
feature comparison table, and Stripe checkout links.
"""

NEW_PRICING = r'''<section data-section-id="pricing" id="pricing" class="py-16 md:py-24 px-4 sm:px-6 bg-white text-[hsl(220,20%,10%)] relative overflow-hidden">
<div class="absolute inset-0 opacity-[0.02]" style="background-image: radial-gradient(rgb(126, 163, 41) 1px, transparent 1px); background-size: 20px 20px;"></div>
<div class="relative max-w-6xl mx-auto text-center">

<!-- Header -->
<div class="inline-block rounded-full bg-[hsl(25,100%,95%)] border border-[hsl(25,80%,80%)] px-5 py-1.5 mb-4"><span class="text-xs font-extrabold uppercase tracking-widest text-[hsl(25,80%,40%)]">Choose Your Plan</span></div>
<h2 class="font-display text-4xl sm:text-5xl lg:text-6xl font-black mb-3 text-[hsl(220,20%,8%)] leading-[1.1]">Data That Pays for Itself.<br><span class="bg-gradient-to-r from-[hsl(78,100%,45%)] to-[hsl(78,80%,35%)] bg-clip-text text-transparent">Pick Your Level.</span></h2>
<p class="text-[hsl(220,10%,45%)] text-lg md:text-xl mb-12 max-w-2xl mx-auto">Every plan includes verified, intent-based contact data. Upgrade to unlock AI agents and full automation.</p>

<!-- 3-Tier Cards -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 mb-16 max-w-5xl mx-auto">

<!-- Tier 1: DataDriver Free -->
<div class="bg-white rounded-2xl p-6 md:p-8 relative overflow-hidden ring-1 ring-[hsl(220,20%,90%)] flex flex-col" style="box-shadow: rgba(0,0,0,0.06) 0px 10px 30px -10px;">
<div class="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-[hsl(220,15%,60%)] to-[hsl(220,15%,75%)]"></div>
<div class="mb-4 mt-2"><span class="text-xs font-extrabold uppercase tracking-widest text-[hsl(220,10%,50%)]">Free</span></div>
<h3 class="font-display text-2xl font-black text-[hsl(220,20%,8%)] mb-1">DataDriver Free</h3>
<p class="text-sm text-[hsl(220,10%,45%)] mb-6">Data acquisition only</p>
<div class="mb-6"><span class="text-5xl font-display font-black text-[hsl(220,20%,8%)]">$0</span><p class="text-sm text-[hsl(220,10%,45%)] mt-1">API rebilling at $0.25/contact</p></div>
<ul class="text-left space-y-3 mb-8 flex-1">
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Dashboard &amp; Analytics</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">15-Source Contact Enrichment</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">CRM Delivery to GHL</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span class="text-sm text-[hsl(220,10%,65%)]">AI Agent Fleet</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span class="text-sm text-[hsl(220,10%,65%)]">Audience Builder</span></li>
</ul>
<a href="https://app.gohighlevel.com/marketplace" target="_blank" rel="noopener" class="inline-flex items-center justify-center w-full rounded-lg bg-[hsl(220,10%,95%)] text-[hsl(220,20%,20%)] font-bold text-base py-3.5 hover:bg-[hsl(220,10%,90%)] transition-colors">Install Free</a>
</div>

<!-- Tier 2: DataDriver Pro (Featured) -->
<div class="bg-white rounded-2xl p-6 md:p-8 relative overflow-hidden ring-2 ring-[hsl(78,60%,75%)] flex flex-col md:-mt-4 md:mb-[-16px]" style="box-shadow: rgba(135, 184, 20, 0.3) 0px 30px 80px -20px, rgba(0, 0, 0, 0.08) 0px 10px 30px -10px;">
<div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r from-[hsl(78,100%,50%)] to-[hsl(78,80%,40%)]"></div>
<div class="absolute -top-20 -right-20 w-48 h-48 bg-[hsl(78,60%,50%)]/5 rounded-full blur-3xl"></div>
<div class="inline-flex items-center gap-2 rounded-full bg-[hsl(78,60%,94%)] border border-[hsl(78,60%,80%)] px-4 py-1.5 mb-4 mt-2 self-start shadow-sm"><span class="w-2 h-2 rounded-full bg-[hsl(78,80%,45%)] animate-pulse"></span><span class="text-xs font-extrabold uppercase tracking-widest text-[hsl(78,70%,28%)]">Most Popular</span></div>
<h3 class="font-display text-2xl font-black text-[hsl(220,20%,8%)] mb-1">DataDriver Pro</h3>
<p class="text-sm text-[hsl(220,10%,45%)] mb-6">Full data stack + 19 Lite agents</p>
<div class="mb-2"><span class="text-5xl font-display font-black text-[hsl(220,20%,8%)]">$497</span><div class="mt-1"><span class="text-lg text-[hsl(220,10%,70%)] line-through">$997/yr</span></div><p class="text-sm text-[hsl(220,10%,45%)] mt-1">one-time &middot; lifetime access</p></div>
<div class="inline-flex items-center gap-2 rounded-full bg-[hsl(78,60%,94%)] border border-[hsl(78,60%,80%)] px-4 py-1.5 mb-6 shadow-sm"><svg class="w-4 h-4 text-[hsl(78,80%,35%)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm font-bold text-[hsl(78,80%,28%)]">14-Day Free Trial Included</span></div>
<ul class="text-left space-y-3 mb-8 flex-1">
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Everything in Free</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]"><strong>19 AI Agents</strong> — Sales + Recruiting</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Sandy SMS Agent</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Voice &amp; Avatar</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span class="text-sm text-[hsl(220,10%,65%)]">Audience Builder</span></li>
</ul>
<a id="dd-checkout-pro" href="https://buy.stripe.com/00w5kC6TTauzbSh9EP0Jq0v" target="_blank" rel="noopener" class="inline-flex items-center justify-center w-full rounded-lg bg-gradient-to-r from-[hsl(78,100%,50%)] to-[hsl(78,80%,40%)] text-[hsl(220,40%,10%)] font-bold text-base py-3.5 hover:from-[hsl(78,100%,45%)] hover:to-[hsl(78,80%,35%)] shadow-lg shadow-[hsl(78,80%,40%)]/25 cta-glow transition-all">Lock Founder Pricing — $497</a>
</div>

<!-- Tier 3: DataDriver Pro+ -->
<div class="bg-white rounded-2xl p-6 md:p-8 relative overflow-hidden ring-2 ring-[hsl(25,80%,75%)] flex flex-col" style="box-shadow: rgba(255, 121, 26, 0.2) 0px 30px 80px -20px, rgba(0, 0, 0, 0.08) 0px 10px 30px -10px;">
<div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r from-[hsl(25,100%,55%)] to-[hsl(15,100%,50%)]"></div>
<div class="absolute -top-20 -right-20 w-48 h-48 bg-[hsl(25,80%,60%)]/5 rounded-full blur-3xl"></div>
<div class="inline-flex items-center gap-2 rounded-full bg-[hsl(25,100%,95%)] border border-[hsl(25,80%,80%)] px-4 py-1.5 mb-4 mt-2 self-start shadow-sm"><span class="text-xs font-extrabold uppercase tracking-widest text-[hsl(25,80%,40%)]">Full Suite</span></div>
<h3 class="font-display text-2xl font-black text-[hsl(220,20%,8%)] mb-1">DataDriver Pro+</h3>
<p class="text-sm text-[hsl(220,10%,45%)] mb-6">Everything + 32 Pro agents</p>
<div class="mb-6"><span class="text-5xl font-display font-black text-[hsl(220,20%,8%)]">$997</span><p class="text-sm text-[hsl(220,10%,45%)] mt-1">one-time + <strong>$199/mo</strong></p></div>
<ul class="text-left space-y-3 mb-8 flex-1">
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Everything in Pro</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]"><strong>32 Pro AI Agents</strong> — Full fleet</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Audience Builder</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Sandy SMS Agent</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Voice &amp; Avatar</span></li>
<li class="flex items-start gap-2.5"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mt-0.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm text-[hsl(220,10%,30%)]">Priority support &amp; onboarding</span></li>
</ul>
<a id="dd-checkout-proplus" href="https://buy.stripe.com/aFa6oGa65fOTcWl04f0Jq0w" target="_blank" rel="noopener" class="inline-flex items-center justify-center w-full rounded-lg bg-gradient-to-r from-[hsl(25,100%,55%)] to-[hsl(15,100%,50%)] text-white font-bold text-base py-3.5 hover:from-[hsl(25,100%,50%)] hover:to-[hsl(15,100%,45%)] shadow-lg shadow-[hsl(25,80%,50%)]/25 cta-glow-orange transition-all">Get Pro+ — $997 + $199/mo</a>
</div>

</div>

<!-- Feature Comparison Table -->
<div class="max-w-4xl mx-auto mb-8">
<h3 class="font-display text-2xl sm:text-3xl font-black text-[hsl(220,20%,8%)] mb-8">Feature Comparison</h3>
<div class="overflow-x-auto rounded-xl ring-1 ring-[hsl(220,20%,92%)]">
<table class="w-full text-left text-sm" style="border-collapse: separate; border-spacing: 0;">
<thead>
<tr class="bg-[hsl(220,15%,97%)]">
<th class="py-3.5 px-5 font-bold text-[hsl(220,20%,25%)] text-left border-b border-[hsl(220,20%,92%)]">Feature</th>
<th class="py-3.5 px-5 font-bold text-[hsl(220,10%,50%)] text-center border-b border-[hsl(220,20%,92%)]">Free</th>
<th class="py-3.5 px-5 font-bold text-[hsl(78,70%,30%)] text-center border-b border-[hsl(220,20%,92%)] bg-[hsl(78,60%,97%)]">Pro</th>
<th class="py-3.5 px-5 font-bold text-[hsl(25,80%,40%)] text-center border-b border-[hsl(220,20%,92%)]">Pro+</th>
</tr>
</thead>
<tbody>
<tr>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-[hsl(220,10%,30%)] font-medium">Dashboard &amp; Analytics</td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center bg-[hsl(78,60%,98%)]"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
</tr>
<tr>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-[hsl(220,10%,30%)] font-medium">Contact Enrichment (15-source)</td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center bg-[hsl(78,60%,98%)]"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
</tr>
<tr>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-[hsl(220,10%,30%)] font-medium">AI Agent Fleet</td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center bg-[hsl(78,60%,98%)]"><span class="text-sm font-bold text-[hsl(78,70%,30%)]">19 agents</span></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><span class="text-sm font-bold text-[hsl(25,80%,40%)]">32 agents</span></td>
</tr>
<tr>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-[hsl(220,10%,30%)] font-medium">Audience Builder</td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center bg-[hsl(78,60%,98%)]"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(25,100%,55%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
</tr>
<tr>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-[hsl(220,10%,30%)] font-medium">Voice &amp; Avatar</td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center bg-[hsl(78,60%,98%)]"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 border-b border-[hsl(220,20%,95%)] text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
</tr>
<tr>
<td class="py-3 px-5 text-[hsl(220,10%,30%)] font-medium">Sandy SMS Agent</td>
<td class="py-3 px-5 text-center"><svg class="w-5 h-5 text-[hsl(220,15%,80%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></td>
<td class="py-3 px-5 text-center bg-[hsl(78,60%,98%)]"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
<td class="py-3 px-5 text-center"><svg class="w-5 h-5 text-[hsl(78,80%,35%)] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></td>
</tr>
</tbody>
</table>
</div>
</div>

</div>
</section>'''

import sys

with open('index.html', 'r') as f:
    content = f.read()

old_start = '<section data-section-id="pricing" id="pricing"'
old_end = '</section><section data-section-id="finalCta"'

start_idx = content.find(old_start)
end_idx = content.find(old_end, start_idx) + len('</section>')

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find pricing section boundaries", file=sys.stderr)
    sys.exit(1)

old_section = content[start_idx:end_idx]

# Flatten the new pricing to a single line (matching pre-rendered style)
new_pricing_flat = ' '.join(NEW_PRICING.split())

new_content = content[:start_idx] + new_pricing_flat + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(new_content)

print(f"Replaced pricing section ({len(old_section)} chars -> {len(new_pricing_flat)} chars)")
print(f"Total index.html: {len(new_content)} chars")
